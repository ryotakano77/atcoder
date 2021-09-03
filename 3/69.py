N, K = tuple(map(int, input().split()))
BIG = 10 ** 9 + 7

if N == 1:
    print(K)
    exit()

if (N, K) == (2, 1):
    print(0)
    exit()

if N == 2:
    print(K * (K - 1))
    exit()

if K <= 2:
    print(0)
    exit()

# (K-2) ** (N-2) % BIGを求める
def calc_remain(k, n, big):
    i = 1
    while k ** i < big:
        i += 1
        if i >= n:
            return (k ** n) % big
    remain = (k ** i) % big
    # k ** i = n + remain
    # k ** i === remain
    div, mod = divmod(n, i)
    # k ** n = k ** (i * div + mod)
    #        = (k ** (i)) ** div * (k ** mod)
    #       === (remain ** div) * (k ** mod)
    return (calc_remain(remain, div, big) * (k ** mod)) % big

ans = K * (K-1) * calc_remain(K-2, N-2, BIG)
ans %= BIG
print(ans)

# print((K * (K-1) * (((K-2) ** (N-2)) % BIG)) % BIG)