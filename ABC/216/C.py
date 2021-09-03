N = int(input())

n_bin = bin(N)[2:]
len_n = len(n_bin)

ans = ""
for e in n_bin:
    if e == "1":
        ans += "AB"
    else:
        ans += "B"

print(ans[:-1])