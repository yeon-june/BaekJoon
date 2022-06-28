import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int,input().split()))

acc = [0] * (N+1)
for a in range(1, N+1):
    acc[a] = acc[a-1] + numbers[a-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(acc[j]-acc[i-1])