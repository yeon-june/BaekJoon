from collections import deque

def bfs(start):
    test = [row[:] for row in t_map]
    queue = deque()
    queue.append(start)
    test[start[0]][start[1]] = 0
    dis = 0
    while queue:
        now = queue.popleft()
        dis = max(dis, test[now[0]][now[1]])
        for m in move:
            new_r, new_c = now[0] + m[0], now[1] + m[1]
            if new_r in range(N) and new_c in range(M) and test[new_r][new_c] == 'L':
                test[new_r][new_c] = test[now[0]][now[1]] + 1
                queue.append((new_r, new_c))

    return dis

move = [(0,1), (0,-1), (1,0), (-1,0)]
N, M = map(int, input().split())
t_map =[]
lands = []
for n in range(N):
    t_map.append(list(input()))
    for m in range(M):
        if t_map[n][m] == 'L':
            lands.append((n,m))

max_dis = 0
for land in lands:
    max_dis = max(max_dis, bfs(land))

print(max_dis)