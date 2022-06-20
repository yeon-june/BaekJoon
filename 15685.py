'''
방향
0세대 : 0
1세대 : 0 1  = (0 , (0+1))
2세대 : 0 1 2 1  = (0, 1, (1+1), (0+1))
3세대 : 0 1 2 1 2 3 2 1 = (0,1,2,1,(1+1),(2+1),(1+1),(0+1))
4세대 : 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1 ...
'''


N = int(input())

# 방향 d에 따른 x, y
dx = [1,0,-1,0] 
dy = [0,-1,0,1]

# 좌표
check = [[0] * (101) for _ in range(101)]


for _  in range(N):
    x,y,d,g = map(int,input().split())

    # 주어진 g세대동안 움직인 방향
    d_list = [d]
    # 먼저 시작하는 x,y 좌표는 방문체크
    check[x][y] = 1

    # 세대 만큼
    for i in range(g):
        tmp = [] #이번 세대 방향 리스트

        for j in range(len(d_list)):
            # 이전 세대들을 돌면서 뒤에서 부터  방향에 1씩 더하고 4로 나눔
            tmp.append((d_list[-j-1]+1)%4)

        d_list.extend(tmp)


    # g 세대 만큼 실행한 뒤 
    # d_list에 있는 방향들을 확인하면서 좌표를 계산해주고, check 처리를 해준다.
    for i in d_list:
        nx = x + dx[i]
        ny = y + dy[i]
        check[nx][ny] = 1 # 체크처리
        x,y = nx,ny # 방향을 현재 움직인 방향으로 갱신

answer = 0
# 100,100 좌표를 돌면서 한 좌표가 1로 체크되어있을 때, 
# 나머지 오른쪽, 아래, 오른쪽 아래대각선이 1로 체크되어있으면
# answer += 1  을 해준다.
for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
            answer += 1

print(answer)