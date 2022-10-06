import unittest
from typing import List

from math import ceil
def theatreSquare(n, m, a):
    x = ceil(n/a)
    y = ceil(m/a)
    return x * y
