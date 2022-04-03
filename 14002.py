# 가장 긴 증가하는 부분 수열 4
# pypy3: 208ms

import sys
from collections import deque

N = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().split()))
dp = [(0,0)] * (N+1)
dp[1] = (1, [lst[1]])
for i in range(2, N+1):
    dp[i] = (1, [lst[i]])
    for j in range(1,i):
        if lst[i] > lst[j]:
            if dp[i][0] > dp[j][0] + 1:
                pass
            else:
                dp[i] = (dp[j][0] + 1, dp[j][1] + [lst[i]])


dp = sorted(dp, key = lambda x: x[0])
print(dp[N][0])
print(*dp[N][1])