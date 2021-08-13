K = int(input())
inf = 10 ** 9 + 7

if K % 9 != 0:
    print(0)
    exit()

ans = [0] * 100010
ans[0] = 1

for i in range(1, 10):
    ans[i] = sum(ans[:i])

if K == 9:
    print(ans[9])
    exit()

for i in range(10, K+1):
    ans[i] = sum(ans[i-9:i]) % inf

print(ans[K])