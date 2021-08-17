N = int(input())

x = []
y = []

for _ in range(N):
    xi, yi = tuple(map(int, input().split()))
    x.append(xi)
    y.append(yi)

x.sort()
y.sort()

div, mod = divmod(N, 2)
if mod == 0:
    ans = (sum(x[div:]) - sum(x[:div])) + (sum(y[div:]) - sum(y[:div]))
else:
    ans = (sum(x[div+1:]) - sum(x[:div])) + (sum(y[div+1:]) - sum(y[:div]))

print(ans)