import pytest


@pytest.mark.parametrize("x,y", [
    (3+5,8),
    (3+4,8),
    (3+6,9),
])

def test_add(x,y):
    assert x==y