# pypy3: 116ms

N = int(input())
price = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = price[1]
for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + price[j]:
            dp[i] = dp[i-j] + price[j]

print(dp[N])