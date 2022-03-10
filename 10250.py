T = int(input())
for t in range(T):
    H, W, N =map(int, input().split())
    if N % H:
        room = N//H + 1
        height = N % H 
    else:
        room = N//H
        height = H

    print(height*100 + room)