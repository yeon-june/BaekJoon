import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N
for i in range(N):
    A[i] = max(A[i]-B,0)
    ans += math.ceil(A[i]/C)

print(ans)