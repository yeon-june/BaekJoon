w, h = map(int, input().split())
init_x, init_y = map(int, input().split())
N = int(input())


# 반복문 안쓰고!
if N % (2*w) > w - init_x:
    if N % (2*w) - w + init_x > w:
        x = (N % (2*w) - 2*w + init_x)
    else:
        x = 2*w -N % (2*w) - init_x

else:
    x = init_x + N % (2*w) 

if N % (2*h) > h - init_y:
    if N % (2*h) - h + init_y > h:
        y = (N % (2*h) - 2*h + init_y)
    else:
        y = 2*h -N % (2*h) - init_y

else:
    y = init_y + N % (2*h) 




print(f'{x} {y}')