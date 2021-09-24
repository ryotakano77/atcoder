P = list(map(int, input().split()))

s = "abcdefghijklmnopqrstuvwxyz"

ans = []

for e in P:
    ans.append(s[e-1])

print("".join(ans))