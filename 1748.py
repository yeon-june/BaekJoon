def N_Digit(N):
    a = N
    cnt = 0
    while a // 10:
        a //= 10
        cnt += 1
    ans = 0
    
    # N이 10의 cnt승일때
    # ans = (N - (10**cnt -1)) * (cnt+1) + 9 * 10**(cnt-1) * (cnt) + ... + 9 * 10**0 
    for i in range(cnt+1):
        ans += 9 * 10**(i-1) * i
    
    ans += (N - (10**cnt -1)) * (cnt+1)

    return int(ans)

N = int(input())
print(N_Digit(N))