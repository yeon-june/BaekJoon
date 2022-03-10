def calcYear(M, N, x, y):
    # k년 -> (k-x) % M == 0 and (k-y) % N == 0
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        
        x += M
        
    return -1
        

T = int(input())
for t in range(T):
    M, N, x, y = map(int, input().split())
    print(calcYear(M, N, x, y))