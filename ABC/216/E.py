import sys
 
sys.setrecursionlimit(10000000)

N, M = tuple(map(int, input().split()))
k = []
a = []
idx = [0] * M
for _ in range(M):
    k.append(int(input()))
    a.append(list(map(int, input().split())))

field = set()
d = dict()

def func(i):
    if idx[i] == k[i]:
        pass
    else:
        # i: aの何番目か
        next = a[i][idx[i]]
        idx[i] += 1

        if not next in field:
            field.add(next)
            d[next] = i

        else:
            # まずはずす
            field.remove(next)
            # 外されたのは次
            func(d[next])
            # 元々も次
            func(i)


for i in range(M):
    func(i)

if len(field) == 0:
    print("Yes")

else:
    print("No")