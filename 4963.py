# 섬의 개수
# pypy3: 200ms

from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    mapp[start[0]][start[1]] = 0

    while queue:
        now = queue.popleft()
        for m in move:
            new_r, new_c = now[0] + m[0], now[1] + m[1]
            if new_r in range(h) and new_c in range(w) and mapp[new_r][new_c]:
                mapp[new_r][new_c] = 0
                queue.append((new_r, new_c))

move = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
w, h = map(int, input().split()) 
while w and h:
    mapp = []
    for _ in range(h):
        mapp.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if mapp[i][j]:
                bfs((i,j))
                cnt += 1

    print(cnt)

    w,h = map(int, input().split())