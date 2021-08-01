N = int(input())
q, mod = divmod(N, 2)

if mod == 1:
    print("")
    exit()

l = [[] for _ in range(q+1)]
l[1] = ["()"]

# (がiこのものを考える
for i in range(2, q+1):
    # 一番左の(と組になる)が右から2j+1番目になるものを考える
    # 左がi-jセット，右がjセット
    # 一番右になるものだけ別
    l[i] += ["(" + e + ")" for e in l[i-1]]
    for j in range(1, i):
        k = i - j
        l_ij = []
        for e_j in l[j]:
            for e_k in l[k]:
                l_ij.append(e_j + e_k)
        
        l[i] += l_ij

ans = set(l[q])
ans = list(ans)
ans = sorted(ans)
for e in ans:
    print(e)