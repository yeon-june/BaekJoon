# 제곱수의 합
# pypy3: 220ms

N = int(input())
dp = [0] * (N+1)
dp[1] = 1

for i in range(2, N+1):
    if int(i**0.5)**2 == i:
        dp[i] = 1
    else:
        dp[i] = i
        for j in range(1, int(i**0.5) + 1):
            dp[i] = min(dp[i], dp[i-j**2] + 1)

print(dp[N])