"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------

import pytest

from stuff.accum import Accumulator


# --------------------------------------------------------------------
# Fixtures (should always return a value)
# -------------------------------------------------------------------
@pytest.fixture  # makes this function a fixture, creates a new accumulator object
def accum():
    return Accumulator() # will pass this value on the function


# --------------------------------------------------------------------
# tests
# -------------------------------------------------------------------

# this tests verifies the accumulator initialize on 0
def test_accumulator_init(accum):  # by adding this parameter, python search for fixture with that name
    assert accum.count == 0


# this tests verifies the accumulator adds 1
def test_accumulator_add_one(accum):
    accum.add()  # calls the accumulator object and its method
    assert accum.count == 1  # verify the count of the object


# this tests verifies the accumulator adds 3 with argument is 3
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


# this tests verifies the accumulator adds two times a 1
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


# this tests verifies the attribute cant be set directly because is a read only property
def test_accumulator_cannot_set_count(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:  #
        # verify the error of the count object
        accum.count = 10
