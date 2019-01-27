import pytest


def add(x,y):
    return x+y

class TestAdd:

    @pytest.mark.run(order=2)
    def test_add1(self):
        assert add(1,2) == 3

    @pytest.mark.run(order=3)
    def test_add2(self):
        assert add(3,5) == 8

    @pytest.mark.run(order=1)
    def test_add3(self):
        assert add(3,5) == 7