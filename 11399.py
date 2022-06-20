# ATM
# pypy3: 112ms

N = int(input())
Pi = list(map(int, input().split()))

Pi = sorted(Pi)
tot = sum(Pi)
for i in range(N):
    tot += Pi[i] * (N-1-i)

print(tot)