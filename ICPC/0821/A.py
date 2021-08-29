circle = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {i : circle[i] for i in range(len(circle))}
dic_rev = {circle[i]: i for i in range(len(circle))}

def solve(num, string):
    index_str = dic_rev[string]
    index_new = index_str - num
    return dic[index_new % len(circle)]

def func(n):
    out = []
    keys = tuple(map(int, input().split()))
    crypt = input()
    for i, s in enumerate(crypt):
        key_i = keys[i % len(keys)]
        out.append(solve(key_i, s))
    return "".join(out)

ans = []
while True:
    N = int(input())
    if N == 0:
        for e in ans:
            print(e)
        exit()
    else:
        ans.append(func(N))