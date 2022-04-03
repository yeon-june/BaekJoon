# 2*n 타일링 2
# pypy3: 104ms

N = int(input())
dp = [0] * (N + 1)
if N < 2:
    dp[1] = 1
elif N < 3:
    dp[1] = 1
    dp[2] = 3

elif N >= 3:
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

print(dp[N] % 10007)