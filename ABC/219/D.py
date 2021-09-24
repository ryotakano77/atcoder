N = int(input())
X, Y = tuple(map(int, input().split()))
AB = []
for _ in range(N):
    A, B = tuple(map(int, input().split()))
    A = min(A, X)
    B = min(B, Y)
    AB.append([A, B])

# まずAについて貪欲
ans = 0
while True:
    AB = sorted(AB, key=lambda x: (-x[0], -x[1]))
    best = AB[0]
    best_a = best[0]
    best_b = best[1]
    X = max(0, X-best_a)
    Y = max(0, Y-best_b)
    ans += 1
    if (X, Y) == (0, 0):
        print(ans)
        exit()
    if ans == N:
        print(-1)
        exit()
    AB_next = []
    for e in AB[1:]:
        a, b = e[0], e[1]
        a = min(X, a)
        b = min(Y, b)
        AB_next.append([a, b])
    AB = AB_next
    