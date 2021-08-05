from itertools import accumulate

N = int(input())
L = 1001
field = [[0 for _ in range(L)] for _ in range(L)]
ans = [0] * (N+1)

for _ in range(N):
    lx, ly, rx, ry = tuple(map(int, input().split()))
    field[lx][ly] += 1
    field[rx][ry] += 1
    field[lx][ry] -= 1
    field[rx][ly] -= 1

# 横方向に累積和
# i行
for i in range(L):
    for j in range(1, L):
        field[i][j] += field[i][j-1]

# 縦方向に累積和
# i列
for i in range(L):
    for j in range(1, L):
        field[j][i] += field[j-1][i]

for i in range(L):
    for j in range(L):
        if field[i][j] > 0:
            ans[field[i][j]] += 1

for e in ans[1:]:
    print(e)