import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1:
            break

        if dp[i][j]:
            nr, nc = i+arr[i][j], j+arr[i][j]
            if nr in range(N):
                dp[nr][j] += dp[i][j]
            if nc in range(N):
                dp[i][nc] += dp[i][j]

print(dp[-1][-1])