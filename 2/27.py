N = int(input())

names = set()
ans = []
for i in range(N):
    s = input()
    if not s in names:
        ans.append(i+1)
        names.add(s)

for e in ans:
    print(e)