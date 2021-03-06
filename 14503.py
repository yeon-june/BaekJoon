'''
pypy3: 108ms
'''

N, M = map(int, input().split())
room =[]

y, x, d = map(int, input().split())
for n in range(N):
    room.append(list(map(int, input().split())))

cnt = 0
move = [(0,-1), (1,0), (0,1), (-1,0)]
while 1:
    if room[y][x] == 0:
        # 1. 현재 위치를 청소한다.
        room[y][x] = 2
        cnt += 1
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    # 2.a 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    # 2.b 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    search_d = 0
    while search_d < 4:
        d = (d-1) % 4 
        if room[y + move[d][1]][x + move[d][0]] == 0:
            x += move[d][0]
            y += move[d][1]
            break
        else:
            search_d += 1

    # 2.c 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    # 2.d 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    if search_d == 4:
        if room[y +(-1)*move[d][1]][x +(-1)*move[d][0]] == 1:
            break
        else:
            x += (-1) * move[d][0]
            y += (-1) * move[d][1]

print(cnt)