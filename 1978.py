N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if num == 1:
        pass
    else:
        for i in range(num-1, 1, -1):
            if num % i == 0:
                break
        else:
            cnt += 1

print(cnt)