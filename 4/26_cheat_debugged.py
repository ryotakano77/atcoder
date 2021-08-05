import sys

sys.setrecursionlimit(10000000)

N = int(input())
colors = [-1] * N
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = (int(e)-1 for e in input().split())
    graph[a].append(b)
    graph[b].append(a)

color0 = []
color1 = []

def dfs(n, color):
    global colors
    colors[n] = color

    if color == 0:
        color0.append(str(n+1))
    else:
        color1.append(str(n+1))

    for next in graph[n]:
        if colors[next] == -1:
            dfs(next, 1-color)

dfs(0, 0)

if len(color0) >= len(color1):
    print(" ".join(color0[:N//2]))
else:
    print(" ".join(color1[:N//2]))