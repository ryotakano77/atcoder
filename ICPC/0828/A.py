def func(k):
    s = input().split(" ")
    num = k // 2
    count = 0
    ok = [("ru", "lu"), ("lu", "ru"), ("rd", "ld"), ("ld", "rd")]
    for i in range(num):
        move = (s[2*i], s[2*i+1])
        if move in ok:
            count += 1

    return count

ans = []

while True:
    k = int(input())
    if k == 0:
        break
    else:
        ans.append(func(k))

for e in ans:
    print(e)