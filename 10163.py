N = int(input())
grid = [[0 for i in range(1001)] for j in range(1001)]

for n in range(N):
    x1, y1, width, height = map(int, input().split())
    for x in range(x1, x1+width):
        for y in range(y1, y1+height):
            grid[y][x] = n+1
    

for n in range(N):
    count = 0
    for row in grid:
        count += row.count(n+1)
    print(count)
