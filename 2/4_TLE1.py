import numpy as np

H, W = (int(e) for e in input().split())

arr = []
arr_w = np.zeros((W))
ans = []
for i in range(H):
    arr_i = np.array([int(e) for e in input().split()])
    arr.append(arr_i)
    ans.append([sum(arr_i)] * W)
    arr_w += arr_i

ans = np.array(ans) + arr_w - np.array(arr)
ans = ans.astype(int).astype(str)

for i in range(H):
    print(" ".join(ans[i]))