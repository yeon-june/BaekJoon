# DFS 스페셜 저지
import sys
from collections import deque
sys.setrecursionlimit(10**5)


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
given = deque(map(int, input().split()))
check = 0
ans = 0


def veri_dfs(visited, given):
    tmp = given.popleft()
    if not given:
        return 1
    visited[tmp] = 1
    for _ in range(len(graph[tmp])):
        if given[0] in graph[tmp] and not visited[given[0]]:
            veri_dfs(visited, given)
    return 0


if given[0] != 1:
    print(0)
elif not veri_dfs(visited, given):
    print(0)
