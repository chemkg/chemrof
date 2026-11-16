"""Check the KGCL change requests in src/data/change_requests.

Each ``.kgcl`` file holds one KGCL command per line; blank lines and lines
starting with ``#`` are comments. This is the format that
``runoak apply --changes-format kgcl`` reads.
"""

import re
from pathlib import Path

import pytest
from kgcl_schema.grammar.parser import parse_statement
from oaklib.utilities.kgcl_utilities import parse_kgcl_files

ROOT = Path(__file__).parent.parent / "src" / "data" / "change_requests"
FILES = sorted(ROOT.rglob("*.kgcl"))
PLACEHOLDER = re.compile(r"\b[A-Za-z][\w.]*:NEW_\w+")


def _commands(path):
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        line = line.strip()
        if line and not line.startswith("#"):
            yield number, line


def _id(path):
    return str(path.relative_to(ROOT))


def test_there_are_change_request_files():
    assert FILES


@pytest.mark.parametrize("path", FILES, ids=_id)
def test_every_command_parses(path):
    failures = []
    for number, command in _commands(path):
        try:
            parse_statement(command)
        except Exception as e:  # the KGCL parser raises several lark exception types
            failures.append(f"{path.name}:{number}: {type(e).__name__}: {command[:80]}")
    assert not failures, "\n".join(failures)


@pytest.mark.parametrize("path", FILES, ids=_id)
def test_runoak_reads_the_same_commands(path):
    with open(path) as f:
        changes = list(parse_kgcl_files([f], changes_format="kgcl"))
    assert len(changes) == len(list(_commands(path)))


@pytest.mark.parametrize("path", FILES, ids=_id)
def test_placeholder_ids_are_created_before_use(path):
    created, problems = set(), []
    for number, command in _commands(path):
        if command.startswith("create node "):
            created.add(command.split()[2])
        for curie in PLACEHOLDER.findall(command):
            if curie not in created:
                problems.append(f"{path.name}:{number}: {curie} used before 'create node'")
    assert not problems, "\n".join(problems)
