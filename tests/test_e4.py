import os
import sys

import pytest

from e4 import in_directory


@pytest.fixture(autouse=True)
def unimport():
    sys.modules.pop('m', None)


@pytest.fixture
def path(tmp_path):
    f = tmp_path / 'm.py'
    f.write_text('x = 1')
    return str(tmp_path)


def test_in_directory(path):
    cwd = os.getcwd()
    assert cwd != path
    with in_directory(path):
        assert os.getcwd() == path
    assert os.getcwd() == cwd


def test_in_directory_import(path):
    with pytest.raises(ImportError):
        import m
    with in_directory(path):
        import m
        assert m.x == 1


def test_in_directory_import_from_cwd(path):
    import conftest
    del sys.modules['conftest']
    with in_directory(path):
        with pytest.raises(ImportError):
            import conftest
