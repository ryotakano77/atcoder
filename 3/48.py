N, K = tuple(map(int, input().split()))

points = []
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    points += [b, a-b]

points.sort(reverse=True)

print(sum(points[:K]))