N = int(input())
a = [0] * 46
b = [0] * 46
c = [0] * 46

for e in tuple(map(int, input().split())):
    rem = e % 46
    a[rem] += 1
for e in tuple(map(int, input().split())):
    rem = e % 46
    b[rem] += 1
for e in tuple(map(int, input().split())):
    rem = e % 46
    c[rem] += 1

ans = 0

for i, numa in enumerate(a):
    for j, numb in enumerate(b):
        for k, numc in enumerate(c):
            if (i + j + k) % 46 == 0:
                ans += numa * numb * numc

print(ans)