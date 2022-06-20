from collections import deque


def bfs(start, col, grid):
    queue = deque()
    queue.append(start)
    grid[start[0]][start[1]] = 0

    while queue:
        now = queue.popleft()
        for m in move:
            new_r, new_c = now[0] + m[0], now[1] + m[1]
            if new_r in range(N) and new_c in range(N) and grid[new_r][new_c] == col:
                queue.append((new_r, new_c))
                grid[new_r][new_c] = 0
                


move = [(0,1), (1,0), (0,-1), (-1,0)]
N = int(input())
paint = [list(input()) for _ in range(N)]
paint_rg = [row[:] for row in paint]
for i in range(N):
    for j in range(N):
        if paint_rg[i][j] == 'G':
            paint_rg[i][j] = 'R'

area = 0
area_rg = 0
for a in range(N):
    for b in range(N):
        if paint[a][b]:
            bfs((a,b), paint[a][b], paint)
            area += 1

        if paint_rg[a][b]:
            bfs((a,b), paint_rg[a][b], paint_rg)
            area_rg += 1

print(area, area_rg)


