# 가장 긴 증가하는 부분 수열

N = int(input())
A = [0] + list(map(int, input().split()))
dp = [1] * (N+1)

for i in range(2, N+1):
    for j in range(1, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
