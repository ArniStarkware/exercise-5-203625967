import sys

import pytest


@pytest.fixture(autouse=True)
def unimport():
    sys.modules.pop('e5', None)


@pytest.mark.xfail
def test_e5_repr():
    import e5
    assert repr(e5) == 'magic module'


@pytest.mark.xfail
def test_e5_call():
    import e5
    assert e5(1) == 1
    assert e5(2) == 2


@pytest.mark.xfail
def test_e5_getitem():
    import e5
    assert e5[1] == 1
    assert e5[2] == 2
