# 메모리: 136468kb
# 시간: 940ms

# deepcopy => [item[:] for item in location]
from collections import deque
from copy import deepcopy
from itertools import combinations

N, M = map(int, input().split())
arr = []
vir_queue = deque()
wall_tmp = []
d=[(0, 1), (0, -1), (1, 0), (-1, 0)]
for n in range(N):
    arr.append(list(map(int, input().split())))
    for m in range(M):
        if arr[n][m] == 2:
            vir_queue.append((n, m))
        elif arr[n][m] == 0:
            wall_tmp.append((n, m))
vir_queue1 = deepcopy(vir_queue)


def bfs():
    while vir_queue:
        x,y = vir_queue.popleft()
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if nx in range(N) and ny in range(M) and arr1[nx][ny] == 0:
                arr1[nx][ny] = 2
                vir_queue.append((nx, ny))


wall_combi = combinations(wall_tmp, 3)
max_safe = 0
for tmp in wall_combi:
    arr1 = deepcopy(arr)
    for point in tmp:
        x, y = point
        arr1[x][y] = 1
    vir_queue = deepcopy(vir_queue1)
    bfs()
    ans = 0
    for row in arr1:
        ans += row.count(0)
    if ans > max_safe:
        max_safe = ans

print(max_safe)