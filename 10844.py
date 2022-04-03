# 쉬운 계단 수
# pypy3: 104ms

N = int(input())
dp = [0] * (N+1)
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, N+1):
    dp[i] = [0] * 10
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % 1000000000
        elif j == 9:
            dp[i][j] = dp[i-1][8] % 1000000000 
        else:
            dp[i][j] = (dp[i-1][j+1] + dp[i-1][j-1]) % 1000000000

print(sum(dp[N]) % 1000000000)