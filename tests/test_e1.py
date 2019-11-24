import subprocess
import sys

import pytest


@pytest.fixture(autouse=True)
def unimport():
    sys.modules.pop('e1', None)


def test_import(capsys):
    import e1
    stdout, stderr = capsys.readouterr()
    assert stdout == "I'm a module!\n"
    assert stderr == ''


def test_execute():
    result = subprocess.run(['python', '../e1.py'], capture_output=True)
    assert result.stdout == b"I'm a script!\n"
    assert result.stderr == b''
