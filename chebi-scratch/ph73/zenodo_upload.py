"""Upload the pH 7.3 bundle to Zenodo (a draft unless --publish is given).

Needs a Zenodo personal access token with the deposit:write scope in
ZENODO_TOKEN. Without --publish, review the draft on zenodo.org (creators,
ORCIDs, description) and publish it there; publishing mints a permanent DOI.

    python zenodo_upload.py data/release/ph73-2026-10-11 [--sandbox]
    python zenodo_upload.py data/release/ph73-2026-10-14 --new-version-of 23324329 [--publish]

--new-version-of makes a new version of an existing deposit (same concept DOI)
and replaces its files. --publish publishes the result (permanent).
"""
import argparse, datetime, json, os, sys
import httpx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('bundle', help='directory written by make_bundle.py')
    ap.add_argument('--sandbox', action='store_true', help='use sandbox.zenodo.org (needs a sandbox token)')
    ap.add_argument('--metadata', default='zenodo_metadata.json')
    ap.add_argument('--new-version-of', type=int, help='deposition id of the version to supersede')
    ap.add_argument('--draft', type=int, help='resume an existing draft deposition (e.g. after a timeout)')
    ap.add_argument('--publish', action='store_true', help='publish the deposit (permanent)')
    a = ap.parse_args()
    token = os.environ.get('ZENODO_TOKEN')
    if not token:
        sys.exit('ZENODO_TOKEN is not set (a Zenodo token with the deposit:write scope)')
    base = 'https://sandbox.zenodo.org/api' if a.sandbox else 'https://zenodo.org/api'
    headers = {'Authorization': f'Bearer {token}'}
    files = sorted(f for f in os.listdir(a.bundle) if os.path.isfile(os.path.join(a.bundle, f)))
    if 'SHA256SUMS' not in files or 'DATACARD.md' not in files:
        sys.exit(f'{a.bundle} does not look like a make_bundle.py output')

    # uploads can take minutes to be acknowledged, so no read timeout
    with httpx.Client(headers=headers, timeout=httpx.Timeout(60, read=None, write=None)) as client:
        if a.draft:
            r = client.get(f'{base}/deposit/depositions/{a.draft}')
            r.raise_for_status()
            dep = r.json()
            if dep['submitted']:
                sys.exit(f'deposition {a.draft} is already published')
            done = {f['filename'] for f in dep.get('files', [])}
            files = [f for f in files if f not in done]
        elif a.new_version_of:
            r = client.post(f'{base}/deposit/depositions/{a.new_version_of}/actions/newversion')
            r.raise_for_status()
            r = client.get(r.json()['links']['latest_draft'])
            r.raise_for_status()
            dep = r.json()
            for f in dep.get('files', []):  # files carried over from the previous version
                client.delete(f"{base}/deposit/depositions/{dep['id']}/files/{f['id']}").raise_for_status()
        else:
            r = client.post(f'{base}/deposit/depositions', json={})
            r.raise_for_status()
            dep = r.json()
        bucket = dep['links']['bucket']
        for f in files:
            with open(os.path.join(a.bundle, f), 'rb') as fh:
                client.put(f'{bucket}/{f}', content=fh).raise_for_status()
            print('uploaded', f)
        with open(a.metadata) as fh:
            meta = json.load(fh)
        meta['metadata'].setdefault('publication_date', datetime.date.today().isoformat())
        r = client.put(f"{base}/deposit/depositions/{dep['id']}", json=meta)
        if r.status_code >= 400:
            sys.exit(f'metadata rejected: {r.text}')
        if a.publish:
            r = client.post(f"{base}/deposit/depositions/{dep['id']}/actions/publish")
            if r.status_code >= 400:
                sys.exit(f'publish failed: {r.text}')
        r = client.get(f"{base}/deposit/depositions/{dep['id']}")
        r.raise_for_status()
        dep = r.json()
    print('deposit:', dep['links']['html'])
    print('DOI:', dep.get('doi') or dep['metadata'].get('prereserve_doi', {}).get('doi'))
    print('state:', dep['state'], '| published:', dep['submitted'])


if __name__ == '__main__':
    main()
