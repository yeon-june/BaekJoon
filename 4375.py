N = int(input())
while N:
    n = 1
    while 1:
        target = int(''.join(['1']*n))
        if target % N == 0:
            print(n)
            break
        n += 1
    # input이 존재할때까지만 
    try:
        N = int(input())
    except:
        break