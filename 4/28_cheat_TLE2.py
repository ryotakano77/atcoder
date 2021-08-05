from itertools import accumulate

N = int(input())
L = 1001
field = [[0 for _ in range(L)] for _ in range(L)]
ans = [0] * (N+1)

for _ in range(N):
    lx, ly, rx, ry = tuple(map(int, input().split()))
    field[lx][ly] = field[lx][ly] + 1
    field[rx][ry] += 1
    field[lx][ry] -= 1
    field[rx][ly] -= 1

# 横方向に累積和
for i in range(L):
    field[i] = list(accumulate(field[i]))

# 縦方向に累積和
for i in range(L):
    column = [field[r][i] for r in range(L)]
    accumulated = list(accumulate(column))
    for i in range(1, N+1):
        ans[i] += accumulated.count(i)

for e in ans[1:]:
    print(e)