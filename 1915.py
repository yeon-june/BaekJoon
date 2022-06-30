N, M = map(int, input().split())
arr = []
ans = 0
for _ in range(N):
    arr.append(list(map(int, list(input().rstrip()))))
    ans = max(arr[-1]+ [ans])

dp = [row[:] for row in arr]

for i in range(1, N):
    for j in range(1, M):
        if arr[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        ans = max(ans, dp[i][j])

print(ans**2)