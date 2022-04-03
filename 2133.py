# 타일 채우기
# pypy3: 104ms

N = int(input())
dp = [0] * (N+1)

if 2<= N < 4:
    dp[2] = 3
elif 4 <= N:
    dp[2] = 3
    dp[4] = 11

    for i in range(5,N+1):
        if i % 2:
            pass
        else:
            dp[i] = dp[i-2] * 3 + 2  # 이전 + 2/ 이번 순번의 고유한 모양
            for j in range(i-2):
                if j % 2 == 0:
                    dp[i] += dp[j] * 2 

print(dp[N])
