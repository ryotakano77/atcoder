K = int(input())

ans = 0
a = 1
while a ** 3 <= K:
    div1, mod1 = divmod(K, a)
    if mod1 == 0:
        b = a
        while b ** 2 <= div1:
            if div1 % b == 0:
                ans += 1

            b += 1

    a += 1

print(ans)