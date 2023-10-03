import pytest


def gen_sum(a, b):
    return a + b


@pytest.mark.skip
def test_method1():
    assert gen_sum(1, 2) == 3


@pytest.mark.xfail
def test_method2():
    assert gen_sum(10, 20) == 40


@pytest.mark.focus
def test_method3():
    assert gen_sum(1,2) != 4