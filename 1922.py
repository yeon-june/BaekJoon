# 네트워크 연결
import heapq

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])

    return parents[x]


def union(x, y):
    px, py = find(x), find(y)
    if px > py: 
        parents[px] = py
    else:
        parents[py] = px


N = int(input())
parents = [i for i in range(N+1)]

M = int(input())
graph = []
for _ in range(M):
    s, e, w = map(int, input().split())
    heapq.heappush(graph, (w, s, e))

ans = 0
while graph:
    w, s, e = heapq.heappop(graph)
    if find(s) != find(e):  # 연결되어있지 않다면
        union(s, e)
        ans += w

print(ans)
