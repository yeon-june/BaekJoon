def tomato(arr, N, M):
    d = [(0,1), (0,-1), (1,0), (-1,0)]
    day = 0
    
    zero = 0
    for row in arr:
        zero += row.count(0)
    if zero == 0:
        return 0
    
    while 1:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    block = 0
                    for k in range(4):
                        if (i+d[k][0] not in range(N)) or (j+d[k][1] not in range(M)):
                            block += 1
                        else:    
                            if arr[i+d[k][0]][j+d[k][1]] == -1:
                                block += 1                
                    if block == 4:
                        return -1

                
                elif arr[i][j] == day+1:
                    for k in range(4):
                        if (i+d[k][0] in range(N)) and (j+d[k][1] in range(M)) and arr[i+d[k][0]][j+d[k][1]] == 0:
                            arr[i+d[k][0]][j+d[k][1]] = day+2
                            
        day += 1
        zero = 0
        for row in arr:
            zero += row.count(0)
        if zero == 0:
            return day



M, N = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int,input().split())))
print(tomato(arr, N, M))