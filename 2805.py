# 이분탐색

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2

    tmp = 0
    for tree in trees:
        tmp += max(tree - mid, 0)

    if tmp >= M:
        start = mid + 1

    else:
        end = mid - 1

print(end)
