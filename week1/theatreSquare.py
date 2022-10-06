import unittest
from typing import List

from math import ceil
def theatreSquare(inputs: List[int]) -> int:
    n, m, a = inputs
    x= ceil(n/a)
    y = ceil(m/a)
    return x*y
