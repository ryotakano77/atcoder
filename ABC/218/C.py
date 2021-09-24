N = int(input())
S = []
T = []
for _ in range(N):
    S.append(list(input().split()))
for _ in range(N):
    T.append(list(input().split()))

# .しかない行，列は削除
def push(graph: list) -> list: 
    r, c = 0, 0
    while True:
        r_i = graph[r]
        if r_i == ["." * N]:
            r += 1
        else:
            break
    while True:
        c_i = [graph[i][0][c] for i in range(N)]
        if c_i == ["."] * (N):
            c += 1
        else:
            break
    r_post, c_post = N-1, N-1
    while True:
        r_i = graph[r_post]
        if r_i == ["." * N]:
            r_post -= 1
        else: 
            break
        c_i = [graph[i][0][c_post] for i in range(N)]
        if c_i == ["."] * N:
            c_post -= 1
        else:
            break
    pushed = []
    for R in range(r, r_post+1):
        pushed.append(graph[R][0][c:c_post+1])
    return pushed

# 時計回りに90度回転
def rotate(graph: list) -> list:
    roteted = []
    row = len(graph)
    column = len(graph[0])
    for r in range(column):
        roteted.append("".join(list(reversed([graph[i][r] for i in range(row)]))))
    return roteted

s = push(S)
t = push(T)

if s == t:
    print("Yes")
    exit()
for _ in range(3):
    t = rotate(t)
    if s == t:
        print("Yes")
        exit()
print("No")