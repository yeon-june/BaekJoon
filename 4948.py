def is_prime(num):
    if num == 1:
        return 0

    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return 0
    
    return 1


N = int(input())
while N:
    cnt =0
    for i in range(N+1, 2*N+1):
        if is_prime(i):
            cnt += 1

    print(cnt)

    N = int(input()) 