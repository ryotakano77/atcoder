ans = []
def func(t, p, r):
    # wrong_num, penalty, correct, team_id
    hist = [[[0] * p, 0, 0, i] for i in range(1, t+1)]
    for _ in range(r):
        l = input().split()
        tid = int(l[0]) - 1
        pid = int(l[1]) - 1
        time = int(l[2])
        mes = l[3]
        if hist[tid][0][pid] == -1:
            continue
        if mes == "CORRECT":
            hist[tid][1] += (hist[tid][0][pid] * 1200) + time
            hist[tid][0][pid] = -1
            hist[tid][2] += 1
        else:
            hist[tid][0][pid] += 1

    sorted_list = sorted(hist, key=lambda x:(-x[2], x[1], x[3]))
    for e in sorted_list:
        ans.append((e[3], e[2], e[1]))

while True:
    T, P, R = tuple(map(int, input().split()))
    if (T, P, R) == (0, 0, 0):
        break
    else:
        func(T, P, R)

for e in ans:
    print(*e)