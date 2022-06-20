# 이모티콘
# pypy3: 264ms
from collections import deque

N = int(input())
# time[r][c] -> r = 이모티콘 개수 c = 클립보드
time = [[-1]*(N+1) for _ in range(N+1)]
time[1][0] = 0
queue = deque()
# 이모티콘 개수, 클립보드
queue.append((1,0))

while queue:
    now = queue.popleft()
    # 복사
    if time[now[0]][now[0]] == -1:
        time[now[0]][now[0]] = time[now[0]][now[1]] + 1
        queue.append((now[0],now[0]))

    # 붙여넣기
    if now[0] + now[1] < N+1 and time[now[0]+now[1]][now[1]] == -1:
        time[now[0]+now[1]][now[1]] = time[now[0]][now[1]] + 1
        queue.append((now[0]+now[1],now[1]))

    # -1
    if now[0] -1 >= 0 and time[now[0]-1][now[1]] == -1:
        time[now[0]-1][now[1]] = time[now[0]][now[1]] + 1 
        queue.append((now[0]-1,now[1]))


ans = 10**10
for i in range(N+1):
    if time[N][i] != -1 and time[N][i] < ans:
        ans = time[N][i]

print(ans)