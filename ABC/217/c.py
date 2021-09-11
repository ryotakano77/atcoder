N = int(input())
p = tuple(map(int, input().split()))
ans = [0] * N

for i in range(N):
    idx = p[i]
    ans[idx-1] = i + 1

print(*ans)