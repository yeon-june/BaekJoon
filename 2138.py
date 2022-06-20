def switch(now, cnt): 
    if cnt == 1: 
        now[0] = 1 - now[0]
        now[1] = 1 - now[1]
    for i in range(1, N-1): 
        if now[i-1] != B[i-1]: 
            cnt += 1 
            now[i-1] = 1 - now[i-1]
            now[i] = 1 - now[i] 
            now[i+1] = 1 - now[i+1] 
    if now[N-2] != B[N-2]:
        cnt += 1 
        now[N-2] = 1 - now[N-2]
        now[N-1] = 1 - now[N-1]
    return cnt if now == B else 10**10


N = int(input()) 
A = list(map(int, input())) 
B = list(map(int,input())) 
res1 = switch(A[:], 0) 
res2 = switch(A[:], 1)

if res1 != 10**10 or res2 != 10**10:
    print(min(res1, res2))
else:
    print(-1)