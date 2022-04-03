# pypy3: 156ms

import sys

dp = [0] * 100001
dp[1], dp[2], dp[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]

for i in range(4, 100001):
    dp[i] = [(dp[i-1][1]+dp[i-1][2])%1000000009, (dp[i-2][0]+dp[i-2][2])%1000000009, (dp[i-3][0]+dp[i-3][1])%1000000009]


T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    print(sum(dp[N])%1000000009)