C, R = map(int, input().split())
K = int(input())

move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
x, y = 0, R 
N = 1
dm = -1
seats = [[0]*C for j in range(R)]
x_length = C
y_length = R

while N <= C*R:
    dm += 1
    count = 1
    if dm % 4 in [0, 2]:
        while count <= y_length:
            x += move[(dm % 4)][0]
            y += move[(dm % 4)][1]
            seats[y][x] = N
            N += 1
            count += 1
        x_length -= 1

    else:
        while count <= x_length:
            x += move[(dm % 4)][0]
            y += move[(dm % 4)][1]
            seats[y][x] = N
            N += 1
            count += 1
        y_length -= 1


if K > R*C:
    print(0)
else:
    for c in range(C):
        for r in range(R):
            if seats[r][c] == K:
                print(c+1, R-r) 

