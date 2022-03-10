# 그리드 필요 없는 부분 지우기
# 사각형 좌표 최소 미만 부분, 최대 초과 부분 지운 정사각형에 대한 반복문 (시간 절약)
N = int(input())

max_grid = 0
min_grid = 1001
squares =[]
for n in range(N):
    x1, y1, width, height = map(int, input().split())
    squares.append([x1, y1, width, height])
    
    if min(x1, y1) < min_grid:
        min_grid = min(x1, y1)

    if max(x1+width, y1+height) > max_grid:
        max_grid = max(x1+width, y1+height)

grid = [[0]*(max_grid - min_grid) for j in range(max_grid - min_grid)]
for i in range(N):
    for h in range(squares[i][3]):
        for w in range(squares[i][2]):
            grid[squares[i][1] - min_grid + h][squares[i][0]-min_grid + w] = i + 1


for k in range(N):
    count =0
    for row in grid:
        count += row.count(k+1)
    print(count)
