T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    flights = [[] for _ in range(N+1)]
    for m in range(M):
        a, b = map(int, input().split())

    print(N-1)
