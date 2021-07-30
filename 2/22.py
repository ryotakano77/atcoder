import math
from functools import reduce

def multi_gcd(*numbers):
    return reduce(math.gcd, numbers)

A, B, C = (int(e) for e in input().split())
gcd = multi_gcd(A, B, C)
A = A // gcd
B = B // gcd
C = C // gcd

print(A + B + C - 3)