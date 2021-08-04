N = int(input())
S = str(input())
len_s = len(S)

INF = (10**9) + 7

goal = "atcoder"
len_goal = len(goal)

# dp[i][j] := Sのi番目までの文字でatcoderのj番目までの文字列を作る作り方
dp = [[0 for _ in range(len_goal + 1)] for _ in range(len_s + 1)]

# i番目で0個まで作るのは必ず1通り
dp[0][0] = 1

for i in range(len_s):
    for j in range(len_goal + 1):
        if j != 7 and S[i] == goal[j]:
            dp[i+1][j+1] += dp[i][j]
        dp[i+1][j] += dp[i][j]

print(dp[len_s][len_goal] % INF)