from simple import read_value, write_value

import pytest
@pytest.fixture
def path(tmp_path):
    n = tmp_path / 'n.txt'
    write_value(n,1)
    s = tmp_path / 's.txt'
    write_value(s,'Hello, world!')
    l = tmp_path / 'l.txt'
    write_value(l, [1, 2, 3, 4, 5])
    return tmp_path


def test_read_values(path):
    n = path / 'n.txt'
    assert read_value(n) == 1
    s = path / 's.txt'
    assert read_value(s) == 'Hello, world!'
    l = path / 'l.txt'
    assert read_value(l) == [1, 2, 3, 4, 5]
