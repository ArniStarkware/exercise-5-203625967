import os
import pathlib
import subprocess
import sys

import pytest


_ROOT = pathlib.Path(__file__).absolute().parent.parent


@pytest.fixture(autouse=True)
def unimport():
    for module in ('p', 'p.x', 'p.y', 'p.x.a', 'p.x.b', 'p.y.c', 'p.y.d'):
        sys.modules.pop(module, None)


def test_package():
    import p
    assert p.__name__ == 'p'
    assert p.__package__ == 'p'


def test_package_init():
    init = _ROOT / 'p' / '__init__.py'
    assert init.exists()


def test_subpackages():
    import p.x
    assert p.x.__name__ == 'p.x'
    assert p.x.__package__ == 'p.x'
    import p.y
    assert p.y.__name__ == 'p.y'
    assert p.y.__package__ == 'p.y'


def test_subpackages_init():
    x_init = _ROOT / 'p' / 'x' / '__init__.py'
    assert x_init.exists()
    y_init = _ROOT / 'p' / 'y' / '__init__.py'
    assert y_init.exists()


def test_submodules():
    import p.x.a
    assert p.x.a.__name__ == 'p.x.a'
    assert p.x.a.__package__ == 'p.x'
    import p.x.b
    assert p.x.b.__name__ == 'p.x.b'
    assert p.x.b.__package__ == 'p.x'
    import p.y.c
    assert p.y.c.__name__ == 'p.y.c'
    assert p.y.c.__package__ == 'p.y'
    import p.y.d
    assert p.y.d.__name__ == 'p.y.d'
    assert p.y.d.__package__ == 'p.y'


def test_submodule_files():
    a = _ROOT / 'p' / 'x' / 'a.py'
    assert a.exists()
    b = _ROOT / 'p' / 'x' / 'b.py'
    assert b.exists()
    c = _ROOT / 'p' / 'y' / 'c.py'
    assert c.exists()
    d = _ROOT / 'p' / 'y' / 'd.py'
    assert d.exists()


def test_api():
    import p
    assert p.A is p.x.A
    assert p.A is p.x.a.A
    assert p.B is p.x.B
    assert p.B is p.x.b.B
    assert p.C is p.y.C
    assert p.C is p.y.c.C
    assert p.D is p.y.D
    assert p.D is p.y.d.D


def test_executable():
    cwd = os.getcwd()
    os.chdir(_ROOT)
    try:
        assert 'usage' in _execute('python', '-m', 'p').lower()
        assert '<p.x.a.A object' in _execute('python', '-m', 'p', 'a')
        assert '<p.x.b.B object' in _execute('python', '-m', 'p', 'b')
        assert '<p.y.c.C object' in _execute('python', '-m', 'p', 'c')
        assert '<p.y.d.D object' in _execute('python', '-m', 'p', 'd')
    finally:
        os.chdir(cwd)


def _execute(*command):
    result = subprocess.run(command, capture_output=True)
    return result.stdout.decode()
