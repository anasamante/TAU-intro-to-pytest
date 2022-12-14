"""
This module contains a basic accumulator class.
Its purpose is to show how to use the pytest framework for testing classes
"""


# ---------------------------------------------------
# Class: Accumulator
# ---------------------------------------------------

class Accumulator:

    def __init__(self):
        self._count = 0  # private variable the initializes on 0

    @property  # this method is a property method, returns the count value, it's a get
    def count(self):
        return self._count

    def add(self, more=1):  # it can change the count value, by default it adds one to the count
        self._count += more
