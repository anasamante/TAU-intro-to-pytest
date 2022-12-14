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
# tests
# -------------------------------------------------------------------

# this tests verifies the accumulator initialize on 0
def test_accumulator_init():
    accum = Accumulator()  # constructs the accumulator object
    assert accum.count == 0


# this tests verifies the accumulator adds 1
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()  # calls the accumulator object and its method
    assert accum.count == 1  # verify the count of the object


# this tests verifies the accumulator adds 3 with argument is 3
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


# this tests verifies the accumulator adds two times a 1
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


# this tests verifies the attribute cant be set directly because is a read only property
def test_accumulator_cannot_set_count():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:  #
        # verify the error of the count object
        accum.count = 10
