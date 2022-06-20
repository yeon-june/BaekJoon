from collections import deque

M, N, K = map(int, input().split())
grid = [[0]*N for _ in range(M)]

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for col in range(c1, c2):
        for row in range(r1, r2):
            grid[row][col] = 1


def bfs(start):
    global area
    queue = deque()
    queue.append(start)
    grid[start[0]][start[1]] = 1

    while queue:
        now = queue.popleft()
        for m in move:
            new_r, new_c = now[0]+m[0], now[1]+m[1]
            if new_r in range(M) and new_c in range(N) and not grid[new_r][new_c]:
                grid[new_r][new_c] = 1
                area += 1
                queue.append((new_r,new_c))
    


move = [(0,1), (1,0), (0,-1), (-1,0)]
ar =[]
for i in range(M):
    for j in range(N):
        if not grid[i][j]:
            area = 1
            bfs((i,j))
            ar.append(area)

ar = sorted(ar)
print(len(ar))
print(*ar)

