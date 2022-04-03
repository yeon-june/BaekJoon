from collections import deque


def solution(idx):
    if idx == N:
        print(*nums)
        return
    if arr[idx][idx] == 0:
        nums[idx] = 0
        solution(idx + 1)
    for k in range(1, 11):
        nums[idx] = arr[idx][idx] * k
        if check(idx) and solution(idx + 1):
            return
    return 


# 부호 & 숫자가 맞는지
def check(idx):
    ssum = 0
    for k in range(idx, -1, -1):
        ssum += nums[k]
        if ssum == 0 and arr[k][idx] != 0:
            return False
        elif ssum < 0 and arr[k][idx] >= 0:
            return False
        elif ssum > 0 and arr[k][idx] <= 0:
            return False

    return True



N = int(input())
lst = deque(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        tmp = lst.popleft()
        if tmp == '+':
            arr[i][j] = 1
        elif tmp == '-':
            arr[i][j] = -1

nums = [0] * N
solution(0)
print(*nums)
