N = int(input())
q, mod = divmod(N, 2)

if mod == 1:
    print("")
    exit()

l = [[] for _ in range(q+1)]
l[1] = ["()"]

# (がiこのものを考える
for i in range(2, q+1):
    l_i = ["("*i + ")"*i]
    # (が左から連続してj個並ぶものを考える
    # 残りは(がi-j個
    for j in range(i-1, 0, -1):
        k = i - j
        l_ij = []
        for e_j in l[j]:
            for e_k in l[k]:
                l_ij.append(e_j + e_k)
        
        l_i += l_ij
    l[i] = l_i

for e in l[q]:
    print(e)