'''
dfs
pypy3: 172ms
python3: Recursion error (416ms - recursion limit expand)

bfs
pypy3: 220ms
python3: 372ms

'''

'''
import sys
sys.setrecursionlimit(10**6)

def dfs(start, g):
    if start[0] not in range(H) or start[1] not in range(W):
        return

    if g[start[0]][start[1]]:
        g[start[0]][start[1]] = 0
    else:
        return

    dfs((start[0]-1, start[1]), g)
    dfs((start[0]+1, start[1]), g)
    dfs((start[0], start[1]-1), g)
    dfs((start[0], start[1]+1), g)


T = int(input())
for t in range(T):
    W, H, N = map(int, input().split())
    ground = [[0]*W for _ in range(H)]

    for n in range(N):
        w, h = map(int, input().split())
        ground[h][w] = 1


    cnt = 0
    for i in range(H):
        for j in range(W):
            if ground[i][j]:
                cnt += 1
                dfs((i,j),ground)
    
    print(cnt)
'''

from collections import deque

def bfs(start, g):
    move = [(0,-1), (0,1), (-1,0), (1,0)]
    queue = deque()
    g[start[0]][start[1]] = 0
    queue.append(start)

    while queue:
        now = queue.popleft()
        for m in move:
            if now[0] + m[0] in range(H) and now[1] + m[1] in range(W) and g[now[0] + m[0]][now[1] + m[1]]:
                queue.append((now[0] + m[0], now[1] + m[1]))
                g[now[0] + m[0]][now[1] + m[1]] = 0



T = int(input())
for t in range(T):
    W, H, N = map(int, input().split())
    ground = [[0]*W for _ in range(H)]

    for n in range(N):
        w, h = map(int, input().split())
        ground[h][w] = 1


    cnt = 0
    for i in range(H):
        for j in range(W):
            if ground[i][j]:
                cnt += 1
                bfs((i,j),ground)
    
    print(cnt)