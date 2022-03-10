# 메모리: 129916 kb
# 시간: 260 ms (pypy3)

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
room = []
vir_l = []
wanted = 0
min_time = N*N
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for n in range(N):
    room.append(list(input().split()))
    for m in range(N):
        if room[n][m] == '2':
            vir_l.append((n,m))
        elif room[n][m] == '0':
            wanted += 1


def bfs(vir_queue):
    global min_time
    vir_infect = 0
    time = 0
    while vir_queue:
        if wanted == vir_infect:
            break
        x, y = vir_queue.popleft()
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if nx in range(N) and ny in range(N):
                if room1[nx][ny] == '0': 
                    room1[nx][ny] = room1[x][y] + 1
                    vir_queue.append((nx, ny))
                    time = room1[nx][ny]
                    vir_infect += 1
                elif room1[nx][ny] == '2':
                    room1[nx][ny] = room1[x][y] + 1
                    vir_queue.append((nx, ny))
                    time = room1[nx][ny]

        if time > min_time:
            return

    if not wanted == vir_infect:
        time = N*N

    min_time = min(time, min_time)
    return
            

active_combi = combinations(vir_l, M)
for combi in active_combi:
    room1 = [row[:] for row in room]

    vir_queue = deque()
    for point in combi:
        x, y = point
        vir_queue.append((x,y))
        room1[x][y] = 0
    bfs(vir_queue)


if min_time == N*N:
    print(-1)
else:
    print(min_time)