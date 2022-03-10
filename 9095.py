# SWEA 종이 붙이기 참고, 점화식
T = int(input())
for t in range(T):
    N = int(input())
    if N <= 3 :
        lst = [0] * 3
        lst[0] = 1
        lst[1] = 2
        lst[2] = 4
        print(lst[N-1])
    else:
        lst = [0] * N
        lst[0] = 1
        lst[1] = 2
        lst[2] = 4
        for i in range(3, N):
            lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
        
        print(lst[N-1])
