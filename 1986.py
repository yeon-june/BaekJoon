def organize(lst, res):
    a = 1
    while a < len(lst):
        res.append((lst[a]-1,lst[a+1]-1))
        a += 2

def place(lst, sym):
    for loc in lst:
        board[loc[0]][loc[1]] = sym

def N_chk(x,y):
    for (dx, dy) in knight_move:
        nx, ny = x+dx, y+dy
        if nx in range(N) and ny in range(M) and board[nx][ny] =='S':
            board[nx][ny] = 'X'

def Q_chk(x,y):
    for (dx, dy) in queen_move:
        now = (x,y)
        while 1:
            nx, ny = now[0]+dx, now[1]+dy
            if nx not in range(N) or ny not in range(M):
                break
            elif board[nx][ny] in ['P', 'N', 'Q']:
                break
            else:
                board[nx][ny] = 'X'
                now = (nx, ny)



knight_move = [(2,1), (-2,1), (2,-1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
queen_move = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
N, M = map(int, input().split())
board = [['S']*M for _ in range(N)]
Queen_tmp = list(map(int, input().split()))
Knight_tmp = list(map(int, input().split()))
Pawn_tmp = list(map(int, input().split()))

Queen = []
Knight = []
Pawn = []

organize(Queen_tmp, Queen)
organize(Knight_tmp, Knight)
organize(Pawn_tmp, Pawn)

place(Queen, 'Q')
place(Knight, 'N')
place(Pawn, 'P')

for n in Knight:
    N_chk(n[0],n[1])

for q in Queen:
    Q_chk(q[0],q[1])

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            ans += 1

print(ans)