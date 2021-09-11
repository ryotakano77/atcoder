L, R = tuple(input().split())

big = 10 ** 9 + 7

digit_l = len(L)
digit_r = len(R)
L = int(L)
R = int(R)

if digit_l == digit_r:
    ans = digit_r * ((L + R) * (R - L + 1) // 2)
    print(ans % big)
    exit()

ans = 0

for digit in range(digit_l, digit_r+1):
    if digit == digit_l:
        l = L
    else:
        l = int("1" + "0"*(digit-1))

    if digit == digit_r:
        r = R

    else:
        r = int("1" + "0"*digit) - 1

    num = (digit * ((l + r) * (r - l + 1) // 2)) % big
    ans += num

print(ans % big)