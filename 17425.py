N = int(input())
for n in range(N):
    A = int(input())
    gA = 0
    for i in range(1, A//2 +1):
        gA += A//i * i
    
    gA += sum(list(range(A//2 + 1, A + 1)))
    print(gA)