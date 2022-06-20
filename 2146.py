# 다리 만들기
# pypy3: 1188ms

from collections import defaultdict, deque
from itertools import combinations


N = int(input())

mapp = [list(map(int, input().split())) for _ in range(N)]
lands = defaultdict(set)

move = [(0,1), (0,-1), (1,0), (-1,0)]
def find_land(r, c):
    global land_num
    
    queue = deque()

    if rep_map[r][c]==1:
        land_num += 1
        queue.append((r,c))
        rep_map[r][c] = -1

    while queue:
        nr, nc = queue.popleft()
        for m in move:
          new_r, new_c = m[0] + nr, m[1] + nc  
          if new_r in range(N) and new_c in range(N):
                if rep_map[new_r][new_c]==1:
                    rep_map[new_r][new_c] = -1
                    queue.append((new_r, new_c))
                elif not rep_map[new_r][new_c]:
                    lands[land_num].add((nr,nc))


land_num = 0
rep_map = [row[:] for row in mapp]
for i in range(N):
    for j in range(N):
        find_land(i, j)

land_com = combinations(lands.keys(),2)


min_dis = 10**10
for a, b in land_com:
    for loc_a in lands[a]:
        for loc_b in lands[b]:
            dis = abs(loc_a[0] - loc_b[0]) + abs(loc_a[1] - loc_b[1]) - 1
            if dis < min_dis:
                min_dis = dis

print(min_dis)