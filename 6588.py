def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True

N = int(input())
while N:
    for i in range(3,N):
        if isPrime(i) and isPrime(N-i):
                print(f'{N} = {i} + {N-i}')
                break
    else:
        print("Goldbach's conjecture is wrong.")
    N = int(input())
