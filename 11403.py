# 플로이드 와샬
# 경로 찾기

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


for k in range(N): # 모든 경유점에 대해
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

for row in arr:
    print(*row)