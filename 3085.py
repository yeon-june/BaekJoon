def row_mx():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1


def col_mx():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if arr[j][i] == arr[j+1][i]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
    

N = int(input())
arr = []
for n in range(N):
    arr.append(list(input()))


ans = 0
for a in range(N):
    for b in range(N-1):
        arr[a][b], arr[a][b+1] = arr[a][b+1], arr[a][b]
        row_mx()
        col_mx()
        arr[a][b], arr[a][b+1] = arr[a][b+1], arr[a][b]

for a in range(N):
    for b in range(N-1):
        arr[b][a], arr[b+1][a] = arr[b+1][a], arr[b][a]
        row_mx()
        col_mx()
        arr[b][a], arr[b+1][a] = arr[b+1][a], arr[b][a]

print(ans)
