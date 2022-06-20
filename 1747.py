def is_prime(x):
    # 중요
    if x == 1:
        return 0

    for i in range(2, x):
        if not x % i:
            return 0
    
    return 1

N = int(input())

while 1:
    tmp = str(N)
    if tmp == tmp[::-1]:
        if is_prime(N):
            break

    N += 1

print(N)