P, K = map(int, input().split())

def is_prime(N):
    for i in range(2, int(N**0.5)+1):
        if not N%i:
            return 0

    return 1

ans = 'GOOD'

for j in range(2,K):
    if (not P%j) and is_prime(j):
        ans ='BAD'
        small = j
        break


if ans =='BAD':
    print(f'{ans} {small}')
else:
    print(ans)