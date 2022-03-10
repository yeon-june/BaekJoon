H, W = map(int, input().split())
weather = []
for h in range(H):
    weather.append(list(input()))

ans = []
for row in range(H):
    ans.append([])
    last_cloud = -1
    for col in range(W):
        if weather[row][col] == 'c':
            last_cloud = col
            ans[row].append(0)
        else:
            if last_cloud >= 0:
                ans[row].append(col-last_cloud)
            else:
                ans[row].append(-1)

for r in ans:
    print(*r)    
