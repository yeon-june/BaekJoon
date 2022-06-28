from math import factorial

T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    less = min(N,M)
    more = max(N,M)

    print(int(factorial(more)/(factorial(less)*factorial(more-less))))
