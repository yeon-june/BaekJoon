# BFS 스페셜 저지
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

given = deque(map(int, input().split()))

ans = 0
def veri_bfs():
    global ans
    rep_given = deque(ins for ins in given)
    visited = [0] * (N+1)
    queue = deque()
    start = rep_given.popleft()
    queue.append(start)
    visited[start] = 1

    while queue:
        if ans:
            break
        now = queue.popleft()
        if rep_given:
            comp = rep_given.popleft()

        while comp in graph[now] and not visited[comp]:
            if comp == given[-1]:
                ans = 1
                break
            visited[comp] = 1
            queue.append(comp)

            if rep_given:
                comp = rep_given.popleft()


if given[0] != 1:
    print(0)

else:
    veri_bfs()
    print(ans)