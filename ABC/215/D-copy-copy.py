def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N, M = tuple(map(int, input().split()))

A = tuple(map(int, input().split()))

primes = set()
for e in A:
    s = set(prime_factorize(e))
    primes = primes.union(s)

counts = set(range(1, M+1))
for p in primes:
    i = 1
    while p * i <= M:
        counts.discard(p*i)
        i += 1

counts = sorted(list(counts))

print(len(counts))
for e in counts:
    print(e)