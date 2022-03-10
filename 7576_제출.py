# bfs 시작점 추가, 서치 새로운 점이 없어질때까지 반복

from collections import deque
M, N = map(int,input().split())
arr = []
queue = deque()
for n in range(N):
    arr.append(list(map(int, input().split())))
    for m in range(M):
        if arr[n][m] ==1:
            queue.append((n,m))

d= [(1,0), (-1,0), (0,1), (0,-1)]

def bfs():
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]
            if nx in range(N) and ny in range(M) and arr[nx][ny] ==0:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

bfs()
ans = 0
for row in arr:
    for k in row:
        if k == 0:
            print(-1)
            exit()
    ans = max(ans, max(row))

print(ans-1)






