# 에라토스테네스의 체

prime = [0 for i in range(10001)]
prime[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        prime[j] = 1

T = int(input())
for t in range(T):
    N = int(input())
    mid = N // 2
    for m in range(mid, 1, -1):
        if prime[m] == 0 and prime[N-m] == 0:
            print(m, N-m)
            break