N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = 0

for ea, eb in zip(a, b):
    ans += abs(ea - eb)

print(ans)