"""Upload the pH 7.3 bundle to Zenodo as a DRAFT deposit (never publishes).

Needs a Zenodo personal access token with the deposit:write scope in
ZENODO_TOKEN. Review the draft on zenodo.org (creators, ORCIDs, description)
and press Publish there; publishing mints a permanent DOI.

    python zenodo_upload.py data/release/ph73-2026-10-11 [--sandbox]
"""
import argparse, json, os, sys
import httpx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('bundle', help='directory written by make_bundle.py')
    ap.add_argument('--sandbox', action='store_true', help='use sandbox.zenodo.org (needs a sandbox token)')
    ap.add_argument('--metadata', default='zenodo_metadata.json')
    a = ap.parse_args()
    token = os.environ.get('ZENODO_TOKEN')
    if not token:
        sys.exit('ZENODO_TOKEN is not set (a Zenodo token with the deposit:write scope)')
    base = 'https://sandbox.zenodo.org/api' if a.sandbox else 'https://zenodo.org/api'
    headers = {'Authorization': f'Bearer {token}'}
    files = sorted(f for f in os.listdir(a.bundle) if os.path.isfile(os.path.join(a.bundle, f)))
    if 'SHA256SUMS' not in files or 'DATACARD.md' not in files:
        sys.exit(f'{a.bundle} does not look like a make_bundle.py output')

    with httpx.Client(headers=headers, timeout=600) as client:
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
        client.put(f"{base}/deposit/depositions/{dep['id']}", json=meta).raise_for_status()
        r = client.get(f"{base}/deposit/depositions/{dep['id']}")
        r.raise_for_status()
        dep = r.json()
    print('draft deposit:', dep['links']['html'])
    print('reserved DOI:', dep['metadata'].get('prereserve_doi', {}).get('doi'))
    print('Not published. Check creators and description, then publish on zenodo.org.')


if __name__ == '__main__':
    main()
