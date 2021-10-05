N = int(input())
A = tuple(map(int, input().split()))
BIG = 998244353

ans = [0] * 10
ans_next = [0] * 10

first, second = A[0], A[1]
ans[(first+second)%10] += 1
ans[(first*second)%10] += 1
if N == 2:
    for e in ans:
        print(e)
    exit()


for i in range(N-2):
    num = A[i+2]
    for j in range(10):
        ans_next[(num + j) % 10] = (ans_next[(num + j) % 10] + ans[j]) % BIG
        ans_next[(num * j) % 10] = (ans_next[(num * j) % 10] + ans[j] % BIG)
    ans = ans_next
    ans_next = [0] * 10

for e in ans:
    print(e % BIG)
