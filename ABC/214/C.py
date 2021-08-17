from itertools import accumulate

N = int(input())
s = tuple(map(int, input().split()))
t = tuple(map(int, input().split()))

dists = [-1 for _ in range(N)]
ans = [-1 for _ in range(N)]

# 初めに渡すのは受け取る＋渡すのmin
st = [s[i]+t[i] for i in range(N)]
min_st = min(st)
idx_first = st.index(min_st)
dists[idx_first] = min_st

for i in range(idx_first+1, idx_first+N):
    if i >= N:
        i -= N
    dists[i] = min(dists[i-1]+s[i], st[i])

for i in range(N):
    ans[i] = min(dists[i-1], t[i])

for e in ans:
    print(e)