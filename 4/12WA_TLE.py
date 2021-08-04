H, W = tuple(map(int, input().split()))
Q = int(input())

field = [[0 for _ in range(W)] for _ in range(H)]
available = [[set() for _ in range(W)] for _ in range(H)]

# 上右下左
X = [0, 1, 0, -1]
Y = [-1, 0, 1, 0]

def q1(h, w):
    global field
    global available

    field[h][w] = 1
    available[h][w].add((h, w))
    after_hw = []
    for dx, dy in zip(X, Y):
        nh, nw = h+dy, w+dx
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        # そこも塗られていたらたどれるところ更新
        if field[nh][nw]:
            after_hw.append((nh, nw))
            available[h][w].add((nh, nw))
            available[h][w] = available[h][w].union(available[nh][nw])

    # 隣り合うところも更新
    for (after_h, after_w) in after_hw:
        available[after_h][after_w].add((h, w))
        available[after_h][after_w] = available[after_h][after_w].union(available[h][w])

def q2(h1, w1, h2, w2):
    if (h2, w2) in available[h1][w1]:
        return "Yes"
    else:
        return "No"

ans = []
for _ in range(Q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        q1(l[1]-1, l[2]-1)
    else:
        ans.append(q2(l[1]-1, l[2]-1, l[3]-1, l[4]-1))

for s in ans:
    print(s)