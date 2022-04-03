'''
pypy3: 156ms
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 0: 가로로 온 수 / 1: 세로로 온 수 / 2: 대각선으로 온 수
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
i = 2

while i < n:
    if arr[0][i]:
        break
    dp[0][0][i] = 1
    i += 1

for i in range(1, n):
    for j in range(2, n):
        # i,j 로 대각선 이동: 일단 i,j 로 이동 가능한지 확인/그 이전 노드들 확인
        if arr[i][j] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
            # i,j 로 갈 수 있는 경우의 수 = 이전 노드 (i-1, j-1)까지 도달하는 모든 경우 (가/세/대각)
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))
        # 대각선 이외 
        if arr[i][j] == 0:
            # i,j 로 가로 이동: 이전이 가로/이전이 대각
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            # i,j 로 세로 이동: 이전이 세로/이전이 대각
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][-1][-1] for i in range(3)))