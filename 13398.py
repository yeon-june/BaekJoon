# 연속합 2
# pypy3: 124ms

N = int(input())
lst = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]
dp[0][0] = lst[0]
dp[1][0] = 0

ans = lst[0] # 전체 다 음수일 때 생각해서 리스트 내 숫자로 하는게 안전
for i in range(1,N):
    dp[0][i] = max(dp[0][i-1]+lst[i], lst[i]) # 아예 아무것도 안지운거
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+lst[i]) # 뭔가 지운거
    ans = max(dp[0][i], dp[1][i], ans)


#print(dp)
print(ans)