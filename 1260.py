'''
pypy3: 216ms
python3: 584ms
'''

from collections import deque, defaultdict
def dfs(start, g, visited):
    print(start, end=' ')
    d_visited[start] = 1

    for n_s in g[start]:
        if not d_visited[n_s]:
            dfs(n_s, g, visited)


def bfs(start, g, visited):
    queue = deque()
    visited.append(start)
    queue.append(start)
    
    while queue:
        now = queue.popleft()
        for next in g[now]:
            if next not in visited:
                visited.append(next)
                queue.append(next)
    
    return visited



N, M, V = map(int, input().split())
edges = defaultdict(list)
for m in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for nodes in edges.values():
    nodes.sort()


d_visited = [0]*(N+1)
b_visited = []

dfs(V, edges, d_visited)
print()
print(*bfs(V,edges, b_visited))