N, L = tuple(map(int, input().split()))

BIG = 10 ** 9 + 7

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    if i <= N - L:
        dp[i + L] = (dp[i+L] + dp[i]) % BIG
    dp[i+1] = (dp[i+1] + dp[i]) % BIG

print(dp[N])