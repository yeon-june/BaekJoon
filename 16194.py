# 카드 구매하기 2
# pypy3: 112ms

N = int(input())
price = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = price[i]
    for j in range(1, i):
        if dp[i] > dp[i-j] + price[j]:
            dp[i] = dp[i-j] + price[j]

print(dp[N])