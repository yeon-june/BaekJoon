# 가장 긴 바이토닉 부분 수열
# pypy3: 132ms

N = int(input())
lst = list(map(int, input().split()))
dp1 = [1] * N
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

dp2 = [1] * N
for a in range(N-1, -1, -1):
    for b in range(N-1, a, -1):
        if lst[a] > lst[b]:
            dp2[a] = max(dp2[a], dp2[b]+1) 

dp = [dp1[k]+dp2[k]-1 for k in range(N)]

print(max(dp))