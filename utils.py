import math
from functools import reduce
from collections import defaultdict

def multi_gcd(*numbers):
    return reduce(math.gcd, numbers)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x], self.d[y])

    def size(self, x):
        return super().size(self.d[x])

    def same(self, x, y):
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.d_inv[self.find(member)]].append(self.d_inv[member])
        return group_members

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

def int_minus(a):
    return int(a) - 1

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

def Eratosthenes2(n: int) -> list:
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


def calc_remain(k, n, big):
    """
    kのn乗をbigで割った余りを求める
    nが大きい時に有効
    """
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