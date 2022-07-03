from collections import deque
import sys
input = sys.stdin.readline

valid = ['.', 'o', 'v']

def bfs(x,y):
    global sheep
    global wolf

    queue = deque()
    sh = 0
    w = 0
    if garden[x][y] == 'o':
        sh += 1
    elif garden[x][y] == 'v':
        w += 1
    queue.append((x,y))    
    garden[x][y] = 0
    
    while queue:
        now = queue.popleft()
        for move in moves:
            nx, ny = now[0] + move[0], now[1] + move[1]
            if nx in range(R) and ny in range(C) and garden[nx][ny] in valid:
                if garden[nx][ny] == 'o':
                    sh += 1
                elif garden[nx][ny] == 'v':
                    w += 1
                garden[nx][ny] = 0
                queue.append((nx, ny))
    
    if sh > w:
        sheep += sh
    else:
        wolf += w



moves = [(0,1), (0,-1), (1,0), (-1,0)]
R, C = map(int, input().split())
garden = []
for _ in range(R):
    garden.append(list(input()))

sheep = 0
wolf = 0

for i in range(R):
    for j in range(C):
        if garden[i][j] in valid:
            bfs(i,j)

print(sheep, wolf)