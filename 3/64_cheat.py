N, Q = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))
diff = [A[i+1] - A[i] for i in range(N-1)]

s = sum([abs(e) for e in diff])
ans = []
for _ in range(Q):
    L, R, V = tuple(map(int, input().split()))
    L -= 1
    R -= 1
    # まず左の処理
    if L > 0:
        pre = diff[L-1]
        diff[L-1] += V
        s += (abs(diff[L-1]) - abs(pre))
    # 右
    if R < N-1:
        pre = diff[R]
        diff[R] -= V
        s += (abs(diff[R]) - abs(pre))
    ans.append(s)

for e in ans:
    print(e)