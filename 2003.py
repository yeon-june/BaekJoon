N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 1
ans = 0
ssum = A[start]
if ssum == M:
    ans += 1

while start < N:
    if ssum < M and end < N:
        ssum += A[end]
        end += 1
    else:
        ssum -= A[start]
        start += 1

    if ssum == M:
        ans += 1

print(ans)