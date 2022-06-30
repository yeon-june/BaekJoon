import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().split())))

dp = [[0]*M for _ in range(N)]
dp[0][0] = maze[0][0]

for a in range(1,M):
    dp[0][a] = dp[0][a-1] + maze[0][a]

for b in range(1, N):
    dp[b][0] = dp[b-1][0] + maze[b][0]

for i in range(1,N):
    for j in range(1,M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + maze[i][j]


print(dp[N-1][M-1])