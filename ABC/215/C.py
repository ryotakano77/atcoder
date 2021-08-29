from itertools import permutations

S, K = input().split()
s = [S[i] for i in range(len(S))]

strs = set()

for perm in permutations(s):
    str_i = "".join(perm)
    strs.add(str_i)

strs = list(strs)
strs.sort()
print(strs[int(K)-1])