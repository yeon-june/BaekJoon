N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
tot = 0

def rev(i,j):
    for n in range(i, i+3):
        for m in range(j, j+3):
            A[n][m] = 1 - A[n][m]


for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            rev(i, j)
            tot += 1
            
        if A == B:
            print(tot)
            exit(0)

if A != B:
    print(-1)
else:
    print(tot)

