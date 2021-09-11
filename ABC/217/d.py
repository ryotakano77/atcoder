from bisect import bisect

L, Q = tuple(map(int, input().split()))
cut = []
ans = []

def c_1(x):
    index = bisect(cut, x)
    cut.insert(index, x)

def c_2(x):
    idx = bisect(cut, x)
    if idx == 0:
        left = 0
    else:
        left = cut[idx-1]
    if idx == len(cut):
        right = L
    else:
        right = cut[idx]
    ans.append(right - left)

for _ in range(Q):
    c, x = tuple(map(int, input().split()))
    if c == 1:
        c_1(x)
    else:
        c_2(x)

for e in ans:
    print(e)