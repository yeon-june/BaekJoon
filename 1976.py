'''
트리의 지름 개념: 
한 노드에서 가장 먼 노드 구하기, 그 노드에서 가장 먼 노드 구하기
1) 임의의 노드에서 가장 먼 노드 구하기
2) 1)번에서 가장 먼 노드의 거리 구하기
pypy3: 204ms
'''
from collections import deque

N = int(input())
weight = [0] * (N+1)
graph =[[] for _ in range(N+1)]
for n in range(N-1):
    par, ch, w = map(int, input().split())
    graph[ch].append((par, w))
    graph[par].append((ch, w))


def bfs(start):
    mx_length =0
    mx_node = 0
    visited = [-1] * (N+1)
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next[0]] == -1:
                visited[next[0]] = visited[now] + next[1]
                queue.append(next[0])
                if visited[next[0]] > mx_length:
                    mx_node = next[0]
                    mx_length = visited[next[0]]

    return [mx_node, mx_length]


from_root = bfs(1)
result = bfs(from_root[0])

print(result[1])

