# passing test
import pytest as pytest


def test_one_plus_one():
    assert 1 + 1 == 2


# failing test
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c


# exception test
def test_divide_by_zero():
    num = 1 / 0


# exception test with .raises, verifies an exception
def test_divide_by_zero_exception():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)
