N, K = tuple(map(int, input().split()))

def Eratosthenes(n: int) -> list:
    """
    2からnまでの整数の素因数の数のlistを返す
    l[i] := iの素因数の数
    """
    num_of_primes = [0] * (n + 1)
    for i in range(2, n+1):
        if num_of_primes[i] != 0:
            continue
        j = 1
        while i * j <= n:
            num_of_primes[i*j] += 1
            j += 1

    return num_of_primes

l = Eratosthenes(N)
ans = 0
for e in l:
    if e >= K:
        ans += 1

print(ans)