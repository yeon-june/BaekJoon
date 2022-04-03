# 이친수
# pypy3: 100ms

N = int(input())
dp = [0] * (N+1)
dp[1] = (0, 1)
for i in range(2, N+1):
    dp[i] = (dp[i-1][0]+dp[i-1][1], dp[i-1][0])

print(dp[N][0]+dp[N][1])