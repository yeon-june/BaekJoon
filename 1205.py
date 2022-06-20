N, S, P = map(int, input().split())
if N == 0:
    print(1)
    exit(0)
scores = list(map(int, input().split()))
scores.append(S)
scores.sort(reverse=True)
rank = scores.index(S) + 1
if rank > P:
    print(-1)
elif (N+1) > P and scores[rank-1] == scores[P]:
    print(-1)
else:
    print(rank)