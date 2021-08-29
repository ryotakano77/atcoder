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

    primes = []
    for i, e in enumerate(num_of_primes):
        if e == 1:
            primes.append(i)

    return primes

N, M = tuple(map(int, input().split()))

A = tuple(map(int, input().split()))

primes = Eratosthenes(M)

def prime_factorize(e):
    s = set()
    i = 0
    while primes[i] <= e:
        if e % primes[i]:
            s.add(primes[i])
        i += 1
    return s

primes_used = set()

for e in A:
    s = prime_factorize(e)
    primes_used = primes_used.union(s)

counts = [0] * (M+1)
for e in primes_used:
    i = 1
    while e * i <= M:
        counts[e*i] = 1
        i += 1

ans = []
for i, e in enumerate(counts[1:]):
    if e == 0:
        ans.append(i+1)

print(len(ans))
for e in ans:
    print(e)