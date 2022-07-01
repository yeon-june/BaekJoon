# 미로의 바운더리 정하기 (x, y의 최대 + 이동, 밟은 곳만 지정하고 나머지는 벽으로 채우기)

import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
note = list(input())

d = 2  # 초기 방향: 남쪽
now = (0, 0)
x_lst = [0]
y_lst = [0]

for move in note:
    if move == 'L':
        d = (d-1) % 4
    elif move == 'R':
        d = (d+1) % 4
    elif move == 'F':
        x, y = now
        nx, ny = x + dx[d], y+dy[d]
        x_lst.append(nx)
        y_lst.append(ny)
        now = (nx, ny)

mx_x, mn_x = max(x_lst), min(x_lst)
mx_y, mn_y = max(y_lst), min(y_lst)
X, Y = mx_x - mn_x + 1, mx_y - mn_y +1
px, py = abs(mn_x), abs(mn_y)
maze = [['#']*Y for _ in range(X)]

for a, b in zip(x_lst, y_lst):
    maze[px+a][py+b] = '.'

for row in maze:
    print(''.join(row))