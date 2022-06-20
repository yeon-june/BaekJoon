# 마법사 상어와 비바라기
# pypy3: 472ms
'''
1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 
   대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
   이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
'''

move = [0, (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)] # 대각선은 2, 4, 6, 8

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]

# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다
now = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for m in magic:
    direct, dis = move[m[0]], m[1]
    move_info = (direct[0]*dis, direct[1]*dis)
    # 구름 이동 & 바구니에 저장된 물의 양이 1 증가
    for i in range(len(now)):
        now[i] = ((now[i][0] + move_info[0]) % N, (now[i][1] + move_info[1]) % N)
        grid[now[i][0]][now[i][1]] += 1

    # 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전
    for k in range(len(now)):
        for j in range(2,9,2):
            c_r, c_c = now[k][0] + move[j][0], now[k][1] + move[j][1]
            if c_r in range(N) and c_c in range(N) and grid[c_r][c_c]:
                grid[now[k][0]][now[k][1]] += 1
    
    can = []
    for h in range(N):
        for l in range(N):
            if grid[h][l] > 1:
                can.append((h,l))
           

    new = []
    # 물의 양이 2 이상인 모든 칸에 구름 (구름이 생기는 칸은 3에서 구름이 사라진 칸이 아님)
    for n in can:
        if n not in now:
            new.append(n)
            grid[n[0]][n[1]] -= 2
    
    now = new


tot = 0
for a in range(N):
    for b in range(N):
        tot += grid[a][b]

print(tot)