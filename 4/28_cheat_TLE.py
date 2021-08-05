import numpy as np

N = int(input())
L = 1001
field = np.array([[0] * L] * L)

for _ in range(N):
    lx, ly, rx, ry = tuple(map(int, input().split()))
    field[lx, ly] += 1
    field[rx, ry] += 1
    field[lx, ry] -= 1
    field[rx, ly] -= 1

for i in range(L):
    field[i, :] = np.cumsum(field[i, :])

for i in range(L):
    field[:, i] = np.cumsum(field[:, i])

for i in range(1, N+1):
    tf = field == i
    print(tf.sum())