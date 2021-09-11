H, W = tuple(map(int, input().split()))
a = []
for _ in range(H):
    a.append(list(map(int, input().split())))
b = []
for _ in range(H):
    b.append(list(map(int, input().split())))

ans = 0
for r in range(H-1):
    for c in range(W-1):
        diff = b[r][c] - a[r][c]
        a[r+1][c] += diff
        a[r+1][c+1] += diff
        a[r][c+1] += diff
        ans += abs(diff)
    if a[r][W-1] != b[r][W-1]:
        print("No")
        exit()

for c in range(W):
    if a[H-1][c] != b[H-1][c]:
        print("No")
        exit()

print("Yes")
print(ans)