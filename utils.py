import math
from functools import reduce

def multi_gcd(*numbers):
    return reduce(math.gcd, numbers)