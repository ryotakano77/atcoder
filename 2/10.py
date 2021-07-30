N = int(input())

c1, c2 = [0], [0]
sum1, sum2 = 0, 0

for _ in range(N):
    c, p = (int(e) for e in input().split())

    if c == 1:
        sum1 += p
    else:
        sum2 += p

    c1.append(sum1)
    c2.append(sum2)

Q = int(input())
ans = []
for _ in range(Q):
    l, r = (int(e) for e in input().split())
    A = str(c1[r] - c1[l-1])
    B = str(c2[r] - c2[l-1])
    ans.append([A, B])

for q in range(Q):
    print(" ".join(ans[q]))