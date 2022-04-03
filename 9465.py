# 스티커
# pypy3: 484ms

T = int(input())
for t in range(T):
    N = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    # 위 사용/ 아래 사용/ 사용 x
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = [stickers[0][0], stickers[1][0], 0]
    for i in range(1, N):
        dp[i] = [max(dp[i-1][1]+stickers[0][i], dp[i-1][2]+stickers[0][i]), max(dp[i-1][0]+stickers[1][i], dp[i-1][2]+stickers[1][i]),max(dp[i-1][0], dp[i-1][1], dp[i-1][2])]

    print(max(dp[-1]))