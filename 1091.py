N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

card = [a % 3 for a in range(N)]
init = P[::]
cnt = 0

if card == P:
    print(cnt)
else:
    while P != card:
        before = P[::]
        for i in range(N):
            P[S[i]] = before[i]
        cnt += 1
        if P == init:
            cnt = -1
            break

    print(cnt)