# 단지번호 붙이기
# pypy3: 148ms

from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    builds = 0
    mapp[start[0]][start[1]] = 0
    builds += 1

    while queue:
        now = queue.popleft()
        for m in move:
            new_r, new_c = now[0] + m[0], now[1] + m[1]
            if new_r in range(N) and new_c in range(N) and mapp[new_r][new_c]:
                mapp[new_r][new_c] = 0
                builds += 1
                queue.append((new_r, new_c))

    return builds

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
mapp = []
for _ in range(N):
    mapp.append(list(map(int, input())))

build_nums = []
cnt = 0
for i in range(N):
    for j in range(N):
        if mapp[i][j]:
            buildings = bfs((i,j))
            cnt += 1
            if buildings:
                build_nums.append(buildings)


build_nums.sort()
print(cnt)
for num in build_nums:
    print(num)