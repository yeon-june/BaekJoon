N, L = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

i = 0
cnt = 0
while i < N:
    tmp = i + 1
    if tmp == N:
        cnt += 1
        break

    for j in range(i+1, N):
        if leak[j] - leak[i] <= L-1:
            if j == N-1:
                cnt += 1 
            
            tmp = j + 1


        else:
            cnt += 1
            break
    
    i = tmp

print(cnt)

