# 동전 0
# pypy3: 120ms

N, K = map(int, input().split())
coins = []
tot = 0
for _ in range(N):
    coins.append(int(input()))

for i in range(N-1, -1, -1):
    tot += K//coins[i]
    K %= coins[i]


print(tot)