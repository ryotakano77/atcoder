from itertools import permutations

def int_minus(a):
    return int(a) - 1

N = int(input())

times = []
for _ in range(N):
    times.append(tuple(map(int, input().split())))

penalty = set()
M = int(input())
for _ in range(M):
    penalty.add(tuple(map(int_minus, input().split())))

perms = permutations(range(N))

big = 10 ** 10
ans = big

def check_perm(perm):
    time_perm = 0
    flag = False
    for i in range(N-1):
        pre = (perm[i], perm[i+1])
        post = (perm[i+1], perm[i])
        flag = flag or (pre in penalty) or (post in penalty)
    if flag:
        return big
    for i in range(N):
        time_perm += times[perm[i]][i]
    return time_perm


for perm in perms:
    ans = min(ans, check_perm(perm))

if ans == big:
    print(-1)
else:
    print(ans)