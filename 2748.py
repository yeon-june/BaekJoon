N = int(input())
Fibonacci =[0] * 91
Fibonacci[1] = 1

if N <= 1:
    print(Fibonacci[N])
else:
    for i in range(2,N+1):
        Fibonacci[i] = Fibonacci[i-1] + Fibonacci[i-2]

    print(Fibonacci[N])