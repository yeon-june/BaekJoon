# 정수삼각형 
# pypy3: 280ms

N = int(input())
triangle = []
for n in range(N):
    front = list(map(int, input().split()))
    triangle.append(front+[0]*(N-1-n))

dp = [[0]*N for _ in range(N)]
dp[0] = [triangle[0][0]] + [0] * (N-1)

for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = dp[i-1][0] + triangle[i][j]

        elif j == N-1:
            dp[i][j] = dp[i-1][N-2] + triangle[i][j]

        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j] 


print(max(dp[-1]))