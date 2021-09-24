def divisor(n):
    l = []
    for i in range(1, n+1):
        if i ** 2 > n:
            break
        div, mod = divmod(n, i)
        if mod == 0:
            l.append(i)
            l.append(div)
    return l

def main():
    N = int(input())
    if N == 0:
        exit()
    ans = N + 2
    divisors = divisor(N)
    for d1 in divisors:
        for d2 in divisors:
            div, mod = divmod(N, d1)
            if mod != 0:
                continue
            div, mod = divmod(div, d2)
            if mod == 0:
                ans = min(ans, d1+d2+div)

    print(ans)

while True:
    main()