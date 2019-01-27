import time
import random
import pytest


def add(x,y):
    return x+y


def test_add3():
    time.sleep(random.randint(2,6))
    pytest.assume(add(4,2,) == 3)
    pytest.assume(add(4, 2) == 6)
    pytest.assume(add(4, 3) == 7)