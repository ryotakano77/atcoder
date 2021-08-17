from collections import deque

H, W = tuple(map(int, input().split()))
r_s, c_s = tuple(map(int, input().split()))
r_g, c_g = tuple(map(int, input().split()))

r_s -= 1
c_s -= 1
r_g -= 1
c_g -= 1

field = []
for _ in range(H):
    field.append(input())

counts = [[-1 for _ in range(W)] for _ in range(H)]
counts[r_s][c_s] = ("", 0)
q = deque([(r_s, c_s)])

# countは(上下からきたかor左右から来たか，曲がった回数)
# "v"は上下から来た，"h"は左右から来た
def bfs(r, c):
    num = counts[r][c][1]
    direction_from = counts[r][c][0]
    # 左右上下
    if not "h" in direction_from:
        c_l = c - 1
        while c_l >= 0:
            if field[r][c_l] == ".":
                if counts[r][c_l] == -1:
                    counts[r][c_l] = ("h", num + ("v" in direction_from))
                    q.append((r, c_l))
                c_l -= 1
            else:
                break

        c_r = c + 1
        while c_r < W:
            if field[r][c_r] == ".":
                if counts[r][c_r] == -1:
                    counts[r][c_r] = ("h", num + ("v" in direction_from))
                    q.append((r, c_r))
                c_r += 1
            else:
                break

    if not "v" in direction_from:
        r_u = r - 1
        while r_u >= 0:
            if field[r_u][c] == ".":
                if counts[r_u][c] == -1:
                    counts[r_u][c] = ("v", num + ("h" in direction_from))
                    q.append((r_u, c))
                r_u -= 1
            else:
                break

        r_d = r + 1
        while r_d < H:
            if field[r_d][c] == ".":
                if counts[r_d][c] == -1:
                    counts[r_d][c] = ("v", num + ("h" in direction_from))
                    q.append((r_d, c))
                r_d += 1
            else:
                break

while q:
    e = q.popleft()
    bfs(*e)
    if e == (r_g, c_g):
        print(counts[r_g][c_g][1])