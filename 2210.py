import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline 

def dfs(x,y,num):
    if len(num) == 6:
        nums.add(num)
        return


    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if nx in range(5) and ny in range(5):
            dfs(nx, ny, num+grid[nx][ny])


grid = []
for _ in range(5):
    grid.append(list(input().split()))

nums = set()
moves = [(0,1), (0,-1), (1,0), (-1,0)]

for i in range(5):
    for j in range(5):
        dfs(i,j,grid[i][j])

print(len(nums))