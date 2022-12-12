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


# parameterized cases
# multiplication cases

# create a list of tuple with the same length
product = [
    (2, 3, 6),  # two positive int
    (1, 99, 99),  # any number by one
    (0, 99, 0),  # by zero
    (3, -4, -12),  # positive by a negative
    (-5, -5, 25),  # negative by a negative
    (2.5, 6.7, 16.75)  # multiply floats
]


@pytest.mark.parametrize('a, b, product', product)
def test_multiply(a, b, product):
    assert a * b == product
