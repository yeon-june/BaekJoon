# 에라토스테네스의 체

N, K = map(int, input().split())

# 1. 2부터 N까지 모든 정수를 적는다.
arr = [1] * (N+1)
arr[0], arr[1] = 0, 0

cnt = 0
# 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
while cnt < K:
    for i in range(2, N+1):
        if arr[i]:
            arr[i] = 0
            erased = i
            cnt += 1
            # print(erased)

            while erased + i <= N:
                if cnt == K:
                    break
                erased += i
                if arr[erased]:
                    arr[erased] = 0
                    cnt += 1
                # print(erased)

        if cnt >= K:
            break


print(erased)      