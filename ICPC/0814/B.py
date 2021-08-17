anss = []
def func(N):
    sets = []
    ans = []
    for _ in range(N):
        sets.append(set(tuple(map(int, input().split()))[1:]))
    search_set = set(tuple(map(int, input().split()))[1:])

    for i, s in enumerate(sets):
        if search_set.issubset(s):
            ans.append(i+1)

    if len(ans) == 1:
        anss.append(ans[0])
    else:
        anss.append(-1)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        func(n)

for e in anss:
    print(e)