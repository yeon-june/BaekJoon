# 마법사 상어와 파이어스톰
# pypy3: 1000ms
from collections import deque

def bfs(start):
    global mx_ice

    queue = deque()
    cnt =0
    
    if ice[start[0]][start[1]]:
        queue.append(start)
        ice[start[0]][start[1]] = 0
        cnt = 1

    while queue:
        now = queue.popleft()
        for d in four_dir:
            new_r, new_c = now[0] + d[0], now[1] + d[1]
            if new_r in range(2**N) and new_c in range(2**N) and ice[new_r][new_c]:
                ice[new_r][new_c] = 0
                cnt += 1
                queue.append((new_r,new_c))

    if cnt > mx_ice:
        mx_ice = cnt


N, Q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2**N)]
l_list = list(map(int, input().split()))
four_dir = [(0,1), (0,-1), (1,0), (-1,0)]

for q in range(Q):
    K = 2**l_list[q]
    new_ice = [[] for _ in range(2**N)]
    # 2L × 2L 크기의 부분 격자로 나누고 돌리기
    for i in range(2**N//K):
        for j in range(2**N//K):
            tmp =[]
            for row in range(i*K, (i+1)*K):
                tmp.append(ice[row][j*K:(j+1)*K])
            rev_tmp = list(map(list, zip(*reversed(tmp))))
            for row1 in range(i*K, (i+1)*K):
                new_ice[row1] += rev_tmp[row1 % K]

    # 주변 얼음 확인
    melt = []
    for a in range(2**N):
        for b in range(2**N):
            adj = 0
            for d in four_dir:
                adj_r, adj_c = a+d[0], b+d[1]
                if adj_r in range(2**N) and adj_c in range(2**N) and new_ice[adj_r][adj_c]:
                    adj += 1
            if adj < 3:
                melt.append((a,b))

    # 얼음 줄이기
    for m in melt:
        new_ice[m[0]][m[1]] = max(0, new_ice[m[0]][m[1]] -1)

    ice = new_ice


tot = 0
for o in range(2**N):
    for p in range(2**N):
        tot += ice[o][p]

mx_ice = 0
for x in range(2**N):
    for y in range(2**N):
        bfs((x,y))
        if mx_ice == 2**N * 2**N:
            print(tot)
            print(mx_ice)
            exit()


print(tot)
print(mx_ice)




    

            

