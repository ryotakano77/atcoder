K = int(input())

ans = 0
c = K
while c ** 3 >= K:
    div1, mod1 = divmod(K, c)
     # a * b = K / c = div1
    b = min(div1, c)
    if mod1 == 0:
        while b ** 2 >= div1 and b <= c:
            if div1 % b == 0:
                ans += 1
            
            b -= 1

    c -= 1

print(ans)