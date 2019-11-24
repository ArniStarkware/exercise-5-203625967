from simple import read_value, write_value


def test_read_values(path):
    n = path / 'n.txt'
    assert read_value(n) == 1
    s = path / 's.txt'
    assert read_value(s) == 'Hello, world!'
    l = path / 'l.txt'
    assert read_value(l) == [1, 2, 3, 4, 5]
