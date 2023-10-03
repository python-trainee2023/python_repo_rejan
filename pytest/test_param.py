import pytest


@pytest.mark.parametrize("a,b,c", [(10, 10, 100), (20, 15, 400)])
def test_method(a, b, c):
    assert a * b == c
