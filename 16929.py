# Two Dots 
# pypy3: 2224 ms
from collections import defaultdict

def dfs(start, visited, cnt):
    global ans
    
    if start == key and cnt !=0:
        ans = 'Yes'
        return

    for next in connection[start]:
        if not visited[next] or (next == key and cnt!=1):
            visited[next] = 1
            dfs(next, visited, cnt+1)
            visited[next] = 0


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

connection = defaultdict(list)
# 연결 찾기
for i in range(N):
    for j in range(M):
        now = board[i][j]
        for k in range(4):
            new_i, new_j = i+di[k], j+dj[k]
            if new_i in range(N) and new_j in range(M) and board[new_i][new_j] == now:
                connection[i*M + j].append(new_i*M + new_j)

ans = 'No'
for key in connection.keys():
    visited = [0] * (N*M)
    visited[key] = 1
    dfs(key, visited, 0)
    if ans == 'Yes':
        break

print(ans)