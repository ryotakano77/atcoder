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

edge_l = int("1" + "0"*digit_l)
num_l = (digit_l * ((L + edge_l - 1) * (edge_l - L) // 2)) % big

edge_r = int("1" + "0"*(digit_r - 1))
num_r = (digit_r * ((edge_r + R) * (R - edge_r + 1) // 2)) % big

ans = num_l + num_r

if digit_r > digit_l + 1:
    for digit_middle in range(digit_l+1, digit_r):
        l = int("1" + "0"*digit_middle)
        r = int("1" + "0"*(digit_middle + 1))
        num_middle = (digit_r * ((l + r - 1) * (r - l) // 2)) % big
        ans += num_middle

print(ans % big)