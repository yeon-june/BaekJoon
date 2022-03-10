from itertools import combinations
from collections import deque

N, M = map(int, input().split())
room = []
vir_l = []
for n in range(N):
    room.append(list(map(int, input().split())))
    for m in range(N):
        if room[n][m] == 2:
            vir_l.append((n,m))

d_v = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
around_n = []
for x, y in vir_l:
    around = 0 
    for direction in d_v:
        nx = x + direction[0]
        ny = y + direction[1]
        if nx in range(N) and ny in range(N) and (room[nx][ny] == 0 or room[nx][ny] == 2):
            around += 1
    
    around_n.append((around,x,y))

around_n = sorted(around_n, key=lambda x : x[0], reverse = True)
com = []
for ar in around_n:
    com.append((ar[1],ar[2]))
    if len(com) == 10:
        break

active_combi = combinations(com, M)

d=[(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs():
    visited = []
    while vir_queue:
        x, y, sec = vir_queue.popleft()
        visited.append((x,y))
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if (nx,ny) not in visited and nx in range(N) and ny in range(N) and (room1[nx][ny] == 0 or room1[nx][ny] == 2):
                room1[nx][ny] = sec + 1
                vir_queue.append((nx, ny, sec + 1))
    return sec


min_time = N*N
for combi in active_combi:
    room1 = [row[:] for row in room]
    cnt_zero = 0
    for row in room1:
        cnt_zero += row.count(0)
    if cnt_zero == 0:
        min_time = 0
        break

    vir_queue =deque()
    for point in combi:
        x, y = point
        vir_queue.append((x,y,0))
        room1[x][y] = 0

    time = bfs()
    cnt_zero = 0
    for row in room1:
        cnt_zero += row.count(0)
    
    if cnt_zero == M and time < min_time:
        min_time = time


if min_time == N*N:
    print(-1)
else:
    print(min_time)