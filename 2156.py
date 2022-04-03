# 포도주 시식
# pypy3: 164ms

N = int(input())
wine = []
for n in range(N):
    wine.append(int(input()))

# 000/ 001/ 010/ 011/ 100/ 101/ 110 (최근 3개 사용 여부) 111은 불가능해서 제외
dp = [[0,0,0,0,0,0,0] for _ in range(N)]
dp[0] = [0, wine[0], 0, wine[0], 0, wine[0], 0]
for i in range(1, N):
    dp[i] = [max(dp[i-1][0], dp[i-1][4]), max(dp[i-1][0], dp[i-1][4]) + wine[i], max(dp[i-1][1], dp[i-1][5]), max(dp[i-1][1], dp[i-1][5]) + wine[i], max(dp[i-1][2], dp[i-1][6]), max(dp[i-1][2], dp[i-1][6]) + wine[i], dp[i-1][3]]

print(max(dp[-1]))