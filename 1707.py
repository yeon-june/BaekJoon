# 이분 그래프
# pypy3: 2648ms
from collections import deque

# bfs
def bfs(start, k):
    queue = deque([start]) 
    visited[start] = k
    while queue:

        now = queue.popleft()

        for i in graph[now]:  # 해당 정점에서 갈 수 있는 하위 정점들을 돈다.
            if not visited[i]:  # 만약 그 정점들을 아직 방문하지 않았다면
                queue.append(i)  # 정점 추가하고
                visited[i] = -1 * visited[now]  # 다른 그룹으로 편성
            elif visited[i] == visited[now]:  # 이미 방문했었는데 같은 그룹이라면
                return 0 
    return 1


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [set() for _ in range(V + 1)]
    visited = [0] * (V + 1) 

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    for i in range(1, V + 1):
        if not visited[i]:
            ans = bfs(i, 1)
            if not ans:
                break

    if ans:
        print('YES')
    else:
        print('NO')