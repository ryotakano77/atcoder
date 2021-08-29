import math

A, B = tuple(map(int, input().split()))

lcm = A * B // math.gcd(A, B)

large = 10 ** 18

if lcm > large:
    print("Large")
else:
    print(lcm)