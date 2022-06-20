from collections import deque
from itertools import combinations

T = int(input())
N, M = map(int, input().split())
house = []
empty = []
for i in range(N):
    house.append(list(input().split()))
    for j in range(N):
        if house[i][j] == '0':
            empty.append((i, j))
        elif house[i][j] == '3':
            sis = (i,j)
        elif house[i][j] == '2':
            me = (i,j) 

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs():
    start = sis
    visited[start[0]][start[1]] = 0
    queue = deque()
    queue.append(start)
    while queue:
        r, c = queue.popleft()
        for m in move:
            nr = r + m[0]
            nc = c + m[1]
            if nr in range(N) and nc in range(N) and case[nr][nc] != '1':
                if case[r][c] == '4':
                    if visited[nr][nc] == '0':
                        visited[nr][nc] = visited[r][c] + 3 
                    else:
                        if visited[nr][nc] > visited[r][c] + 3:
                            visited[nr][nc] = visited[r][c] + 3

                elif case[r][c] == '0' or case[r][c] == '3':
                    if visited[nr][nc] == '0':
                        visited[nr][nc] = visited[r][c] + 1 
                    else:
                        if visited[nr][nc] > visited[r][c] + 1:
                            visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
                if (nr, nc) == me:
                    return


chair_combi = combinations(empty, M)
max_time = 0
ans = 0
for tmp in chair_combi:
    case = [row[:] for row in house]
    for (a, b) in tmp:
        case[a][b] = '4'
    visited = [['0'] * N for _ in range(N)]
    bfs()
    if visited[me[0]][me[1]] == '0':
        ans = 'SAFE'
        break
    elif visited[me[0]][me[1]] >= T:
        ans = 'SAFE'
        break
    else:
        if visited[me[0]][me[1]] > max_time:
            max_time = visited[me[0]][me[1]]


if ans == 'SAFE':
    print(ans)
else:
    print('GOOD LUCK', T - max_time)

