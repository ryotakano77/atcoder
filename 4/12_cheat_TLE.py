from collections import defaultdict
from itertools import product

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

class UnionFindField(UnionFindLabel):

    def __init__(self, H: int, W: int):
        self.H, self.W = H, W
        coordinates = [p for p in product(range(H), range(W))]
        super().__init__(coordinates)
        self.flags = [[0] * W for _ in range(H)]

    def flag_on(self, r, c):
        self.flags[r][c] = 1

    def is_flag_on(self, r, c):
        return self.flags[r][c]

    def find_flag_on_adjacent(self, r, c):
        # 上右下左
        X = [0, 1, 0, -1]
        Y = [-1, 0, 1, 0]
        for dx, dy in zip(X, Y):
            nr, nc = r+dx, c+dy
            # 探す範囲がfield外なら考えない
            if nr < 0 or nr >= self.H or nc < 0 or nc >= self.W:
                continue
            if not self.flags[nr][nc]:
                continue
            self.union((r, c), (nr, nc))

H, W = tuple(map(int, input().split()))
Q = int(input())

uff = UnionFindField(H, W)

ans = []
for _ in range(Q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        uff.flag_on(l[1]-1, l[2]-1)
        uff.find_flag_on_adjacent(l[1]-1, l[2]-1)
    else:
        if uff.is_flag_on(l[1]-1, l[2]-1) and uff.is_flag_on(l[3]-1, l[4]-1) and uff.same((l[1]-1, l[2]-1), (l[3]-1, l[4]-1)):
            ans.append("Yes")
        else:
            ans.append("No")

for s in ans:
    print(s)