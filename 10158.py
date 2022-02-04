def ant_move(w,h,init_x,init_y,N):
    x = 1
    y = 1
    trans = -1
    
    while N > 0:
        if (not 0 <= init_x + x <= w) and (not 0 <= init_y + y <= h):
            x *= trans
            y *= trans
        elif not 0 <= init_x + x <= w:
            x *= trans
        elif not 0 <= init_y + y <= h:
            y *= trans
        
        init_x += x
        init_y += y
        N -= 1

    return print(f'{init_x} {init_y}')

w, h = map(int, input().split())
init_x, init_y = map(int, input().split())
N = int(input())

ant_move(w,h,init_x,init_y,N)