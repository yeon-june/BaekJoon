# 여러개의 입력으로 이루어짐
while True:
    try:
        X = int(input()) * 10000000
        N = int(input())
        legos = [int(input()) for _ in range(N)]
        legos.sort()
        
        found = False
        i, j = 0, N-1
        while i < j:
            if legos[i] + legos[j] == X:
                print(f'yes {legos[i]} {legos[j]}')
                found = True
                break
            
            elif legos[i] + legos[j] < X:
                i += 1
            else:
                j -= 1
            
        if not found:
            print('danger')

    except:
        break

    