def up_down(N, broken_lst, init_ch):
    up_ch = N
    down_ch = N
    while 1:
        # down, up 순서 중요
        if down_ch >= 0:
            for num in str(down_ch):
                if int(num) in broken_lst:
                    down_ch -= 1
                    break
            else:
                min_move = abs(down_ch - N) + len(str(down_ch))
                break

        for num in str(up_ch):
            if int(num) in broken_lst:
                up_ch += 1
                break
        else:
            min_move = abs(up_ch - N) + len(str(up_ch))
            break

        if abs(up_ch - N) + len(str(up_ch)) > abs(init_ch -N):
            min_move = abs(init_ch -N)
            break
        
    
    return min_move
    

N = int(input())
broken_n = int(input())
if broken_n ==0:
    broken_lst = []
else:
    broken_lst = list(map(int, input().split()))
init_ch = 100
exc_ch = [98, 99, 100, 101, 102, 103]



if N in exc_ch:
    ans = abs(init_ch - N)
elif broken_n == 10:
    ans = abs(init_ch - N)
else:
    ans = up_down(N, broken_lst, init_ch)

print(ans)
                
