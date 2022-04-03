# 가장 큰 증가 부분 수열
# pypy3: 116ms

N = int(input())
lst = list(map(int, input().split()))
dp = [0] * N
dp[0] = lst[0]
for i in range(1,N):
    dp[i] = lst[i]
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[j]+lst[i], dp[i])

print(max(dp))