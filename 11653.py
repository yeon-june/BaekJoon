N = int(input())
if N != 1:
    for i in range(2, int(N**0.5) + 1):
        while not N % i:
            print(i)
            N //= i

if N != 1:
    print(N)