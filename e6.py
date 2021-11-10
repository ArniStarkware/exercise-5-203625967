from simple import mul, div, greet, write_value, read_value

import pytest

def test_mul():
    for a in range(1,10):
        for b in range(1,10):
            assert mul(a,b) == a * b


def test_mul_zero():
    for a in range(1,10):
        assert mul(a,0) == 0
        assert mul(0,a) == 0


def test_mul_negative():
    for a in range(-10,-1):
        for b in range(1,10):
            assert mul(a,b) == a * b
            assert mul(a, -b) == - a * b


def test_mul_fraction():
    for a in range(1,10):
        assert mul(a, 3.1415) == a * 3.1415
        assert mul(3.1415, a) == 3.1415 * a


def test_div():
    for a in range(1,10):
        for b in range(1,10):
            assert div(a,b) == a / b


def test_div_negative():
    for a in range(-10,-1):
        for b in range(1,10):
            assert div(a,b) == a / b
            assert div(a, -b) == - a / b


def test_div_fraction():
    for a in range(1,10):
        assert div(a, 3.1415) == a / 3.1415
        assert div(3.1415, a) == 3.1415 / a


def test_div_error():
    with pytest.raises(ZeroDivisionError):
        div(3.1415,0)



def test_greet(capsys):
    for name in ['Sara','Yuda','Zoidexer']:
        greet(name)
        stdout, stderr = capsys.readouterr()
        assert stdout == 'Hello, '+name+'!\n'
        assert stderr == ''


def test_greet_stranger(capsys):
    greet()
    stdout, stderr = capsys.readouterr()
    assert stdout == 'Hello, stranger!\n'
    assert stderr == ''


def test_read_value_int(tmp_path):
    for i in range(10):
        f = tmp_path / 'file.txt'
        write_value(f,i)
        assert read_value(f) == i


def test_read_value_str(tmp_path):
    for i in ['foo','bar']:
        f = tmp_path / 'file.txt'
        write_value(f,i)
        assert read_value(f) == i


def test_read_value_list(tmp_path):
    for i in [[1,2,3],[]]:
        f = tmp_path / 'file.txt'
        write_value(f,i)
        assert read_value(f) == i
