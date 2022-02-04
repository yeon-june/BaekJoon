# 색칠하기

#그리드 만들기
grid = [[0 for i in range(100)] for j in range(100)]

#사각형 정보 받기
for k in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    # 색칠..색칠..색칠..
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[y][x] = 1

#넓이 구하기
count = 0
for row in grid:
    count += sum(row)

print(count)