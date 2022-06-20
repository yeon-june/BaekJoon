import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
visited = [0]*N
check = 0
cycle = []
distance = [10**10]*N

def getcycle(x,path):
    global cycle
    global check
    # 이미 찾았으면 더 이상 찾지 않음
    if check:
        return
    for station in graph[x]:
        if not visited[station]:
            visited[station] = 1
            path.append(station)
            getcycle(station,path)
            visited[station] = 0
            path.pop()
        elif len(path) >= 3 and path[0] == station:
            check = 1
            cycle = path[:]
            return


# 사이클 아닌 점들 거리
def bfs(x):
    queue = deque([x])
    
    while queue:
        start = queue.popleft()
        for end in graph[start]:
            if distance[end] != 0 and not visited[end]:
                distance[end] = distance[start] + 1
                queue.append(end)
                visited[end] = True
                
for x in range(N):
    if not check:
        visited[x] = 1
        getcycle(x,[x])
    else:
        break
    
for i in cycle:
    distance[i] = 0

visited = [0]*N
for i in cycle:
    visited[i] = 1
    bfs(i)    

print(*distance)    