N, M, K = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))

# 동, 남, 서, 북
d = [(0,1), (1,0), (0,-1), (-1,0)]
direct = 0
t = 1
f = 6
# 동, 남, 서, 북
side = [3, 5, 4, 2]

def opposite(direct):
    if direct == 0:
        return 2
    elif direct == 1:
        return 3
    elif direct == 2:
        return 0
    else:
        return 1
    

def turn_dice(t,f,side,direct):
    nt = side[direct]
    nf = 7 - nt
    side[direct] = t
    if direct % 2:
        if direct == 1:
            side[3] = f
        else:
            side[1] = f
    else:
        if direct == 0:
            side[2] = f
        else:
            side[0] = f
    
    t = nt
    f = nf

row = 0
column = 0
cnt =0
score = 0

while cnt < K:
    nr = row + d[direct][0]
    nc = column + d[direct][1]
    if nr in range(N) and nc in range(M):
        row = nr
        column = nc

    else:
        direct = opposite(direct)
        row = row + d[direct][0]
        column = column + d[direct][1]

    turn_dice(t,f,side,direct)
    print(row, column)
    B = arr[row][column]
    tr = row
    tc = column
    queue = [(tr,tc)]
    visited = []
    bfcnt = 1
    while queue:
        x, y = queue.pop()
        for move in d:
            nx = x + move[0]
            ny = y + move[1]
            if (nx, ny) not in visited and nx in range(N) and ny in range(M) and arr[nx][ny] == B:
                visited.append((x,y))
                queue.append((nx,ny))
                bfcnt += 1
    
    C = bfcnt

    score += B*C

    if B < f:
        direct = (direct + 1) % 4
    elif B > f:
        direct = (direct - 1) % 4
    else:
        pass

    cnt += 1

print(score)