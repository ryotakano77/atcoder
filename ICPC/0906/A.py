def main(d, e):
    distance = 10 ** 9
    for x in range(d+1):
        y = d - x
        dist_i = abs(((x**2 + y**2) ** (0.5)) - e)
        distance = min(distance, dist_i)

    return distance

ans = []
while True:
    D, E = tuple(map(int, input().split()))

    if (D, E) == (0, 0):
        break
    else:
        ans.append(main(D, E))

for e in ans:
    print(e)