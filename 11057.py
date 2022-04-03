# 오르막수
# pypy3: 120ms

N = int(input())
dp = [[0]*10 for _ in range(N)]
dp[0] = [1] * 10
for i in range(1,N):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])%10007

print(sum(dp[-1])%10007)