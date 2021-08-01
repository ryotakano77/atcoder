N, K = (int(e) for e in input().split())

A = [int(e) for e in input().split()]
B = [int(e) for e in input().split()]

sum_diff = 0
for i in range(N):
    diff = abs(A[i] - B[i])
    sum_diff += diff

if K < sum_diff:
    print("No")
    exit()

remainder = (K - sum_diff) % 2

if remainder:
    print("No")

else:
    print("Yes")