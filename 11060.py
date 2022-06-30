import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [10**10] * N
dp[0] = 0

for i in range(N):
    for j in range(1, A[i]+1):
        if i+j < N:
            dp[i+j] = min(dp[i+j], dp[i] + 1)
        else: break

if dp[-1] == 10**10:
    print(-1)
else:
    print(dp[-1])