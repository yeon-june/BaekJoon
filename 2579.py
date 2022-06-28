# [이전계단 x, 이전계단 o]

N= int(input())
stairs = [0]*N
for i in range(N):
    stairs[i] = int(input())

dp = [[0,0] for _ in range(N)]
dp[0][0] = stairs[0]

for j in range(1, N):
    dp[j][0] = max(dp[j-2])+stairs[j]
    dp[j][1] = dp[j-1][0] + stairs[j]

print(max(dp[-1]))