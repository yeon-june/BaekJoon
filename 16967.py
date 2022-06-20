H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]

A=[]
for i in range(H):
    A.append([])
    for j in range(W):
        A[i].append(B[i][j])

for n in range(X,H):
    for m in range(Y,W):
        A[n][m] -= A[n-X][m-Y]

for row in A:
    print(*row)