from collections import defaultdict
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
dx = defaultdict(list)
dy = defaultdict(list)

for _ in range(N):
    x, y = tuple(map(int, input().split()))
    dx[x].append(y)
    dy[y].append(x)

ans = 0

for x, ys in dx.items():
    if len(ys) < 2:
        continue
    dys = defaultdict(int)
    for y in ys:
        for x_of_y in dy[y]:
            dys[x_of_y] += 1
    del dys[x]
    for xs in dys.values():
        if xs == 1:
            continue
        else:
            ans += combinations_count(xs, 2)

print(ans // 2)