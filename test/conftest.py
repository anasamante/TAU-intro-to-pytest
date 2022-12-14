# --------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------
import pytest

from stuff.accum import Accumulator


# --------------------------------------------------------------------
# Fixtures (should always return a value)
# -------------------------------------------------------------------
@pytest.fixture  # makes this function a fixture, creates a new accumulator object
def accum(): # if we add (scope="session") it runs once for the entire suite
    print("this is the setup part")
    yield Accumulator()  # will pass this value on the function
    print("this is the cleanup part")
