from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    case[x][y] = 0

    while queue:
        now = queue.popleft()
        for move in moves:
            nx, ny = now[0] + move[0], now[1] + move[1]
            if nx in range(N) and ny in range(N) and case[nx][ny]:
                queue.append((nx,ny))
                case[nx][ny] = 0


N= int(input())
arr = []
mx_rain = 0
moves = [(1,0), (-1,0), (0,1), (0,-1)]
for _ in range(N):
    A = list(map(int, input().split()))
    arr.append(A)
    mx_rain = max(max(A), mx_rain)

rain = 1
mx_safe = 1
while rain <= mx_rain-1:
    for i in range(N):
        for j in range(N):
            arr[i][j] = max(arr[i][j]-1,0)
    
    case = [row[:] for row in arr]
            
    safe = 0
    for x in range(N):
        for y in range(N):
            if case[x][y]:
                safe += 1
                bfs(x,y)


    if safe > mx_safe:
        mx_safe = safe 

    rain += 1

print(mx_safe)