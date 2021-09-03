N = int(input())

names = set()
for _ in range(N):
    t = tuple(input().split())
    names.add(t)

if len(names) == N:
    print("No")
else:
    print("Yes")