import sys
input = sys.stdin.readline

R, C = map(int, input().split())
room =[['*']*C for _ in range(R)]

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    room[a][b] = 'X'

(sr,sc) = map(int, input().split())

moves = list(map(int, input().split()))
direct = [(-1,0), (1,0), (0,-1), (0,1)]

now = (sr,sc)
room[sr][sc]= 0
d = 0
turn = 0
while 1:
    (r, c) = direct[moves[d]-1]
    new_r, new_c = now[0] + r, now[1] + c
    if (new_r in range(R)) and (new_c in range(C)):
        if room[new_r][new_c] == '*':
            now = (new_r, new_c)
            room[new_r][new_c] = 0
            turn = 0
        else:
            d = (d+1)%4
            turn += 1
            if turn ==4:
                break

    else:
        d = (d+1)%4
        turn += 1
        if turn == 4:
            break

print(*now)
        