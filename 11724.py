# 연결 요소의 개수
# pypy3: 1168ms

from collections import defaultdict

def visit(start):
    visited.append(start)

    for next in graph[start]:
        if next not in visited:
            visit(next)


N, M = map(int, input().split())
graph = defaultdict(list)
for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
cnt = 0

for i in range(1, N+1):
    if i not in visited:
        visit(i)
        cnt += 1

print(cnt)
