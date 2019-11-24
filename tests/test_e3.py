import types

import pytest

from e3 import load


_NAME = 'm'
_FILE = f'{_NAME}.py'
_CODE = '''
x = 1
def hello():
    return 'Hello, world!'
'''


@pytest.fixture
def m(tmp_path):
    f = tmp_path / _FILE
    f.write_text(_CODE)
    return load(str(f))


def test_module(m):
    assert isinstance(m, types.ModuleType)


def test_name(m):
    assert m.__name__ == _NAME


def test_code(m):
    assert m.x == 1
    assert m.hello() == 'Hello, world!'
