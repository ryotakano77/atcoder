from collections import deque

N = int(input())

roads = [[] for _ in range(N)]

for _ in range(N-1):
    A, B = (int(e) - 1 for e in input().split())
    roads[A].append(B)
    roads[B].append(A)

def dfs(city_num: int) -> list:
    path_length = [1 if i in roads[city_num] else 0 for i in range(N)]
    
    # まずはcity_numが行けるところから考え始める
    queue = deque(roads[city_num])
    while queue:
        search_city = queue.popleft()
        search_length = path_length[search_city]
        for city_from_search in roads[search_city]:
            if path_length[city_from_search]:
                pass
            else:
                path_length[city_from_search] = search_length + 1
                queue.append(city_from_search)

    return path_length

length_1 = dfs(0)
max_from_1 = length_1.index(max(length_1))
length_max = dfs(max_from_1)
print(max(length_max) + 1)