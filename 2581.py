# 소수
def is_prime_number(num):
    if num == 1:
        return 0
    # 확인
    for i in range(2, num):
        if not num % i:
            return 0

    return 1

M = int(input())
N = int(input())
min_prime = 0
prime_sum = 0
for a in range(M, N+1):
    if is_prime_number(a):
        prime_sum += a
        if not min_prime:
            min_prime = a

if not min_prime:
    print(-1)
else:
    print(prime_sum)
    print(min_prime)