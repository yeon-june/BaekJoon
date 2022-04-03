# 1로 만들기
# pypy3: 136ms

N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # 1 빼기
    
    if not i % 3:
        dp[i] = min(dp[i], dp[i//3] + 1)  # 3 나누기

    if not i % 2:
        dp[i] = min(dp[i], dp[i//2] + 1)  # 2 나누기

print(dp[N])

