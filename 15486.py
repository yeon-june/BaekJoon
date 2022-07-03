import sys
input = sys.stdin.readline

N = int(input())
T = [0] * N
P = [0] * N
for a in range(N):
    t, p = map(int, input().split())
    T[a] = t
    P[a] = p

dp =[0] * (N+1)

for i in range(N):
    if T[i] <= N-i:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])

    dp[i+1] = max(dp[i+1], dp[i])

print(dp[-1])