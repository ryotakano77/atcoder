N = int(input())
a = []
for _ in range(N):
    l = list(map(int, input().split()))
    a.append(sum(l))

ans = 1
for e in a:
    ans *= e

print(ans % (10 ** 9 + 7))