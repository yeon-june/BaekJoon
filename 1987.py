R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
grid_num = [[0]*C for _ in range(R)] 
for i in range(R):
    for j in range(C):
        grid_num[i][j] = ord(grid[i][j]) - 65

visited = [0] * 27

move = [(0,1), (0,-1), (1,0), (-1,0)]
mx_move = 0

def dfs(start,cnt):
    global mx_move

    for m in move:
        new_r, new_c = start[0] + m[0], start[1] + m[1]
        if new_r in range(R) and new_c in range(C) and not visited[grid_num[new_r][new_c]]:
            visited[grid_num[new_r][new_c]] = 1
            dfs((new_r, new_c), cnt + 1)
            visited[grid_num[new_r][new_c]] = 0
    
    else:
        if mx_move < cnt:
            mx_move = cnt

visited[grid_num[0][0]] = 1
dfs((0,0), 1)

print(mx_move)
