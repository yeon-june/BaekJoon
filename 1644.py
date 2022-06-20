# 소수의 연속합
N = int(input())
era = [1] * (N+1)
era[0], era[1] = 0, 0
prime_lst = []

for i in range(N+1):
    if era[i]:
        prime_lst.append(i)
        era[i] = 0
        now = i

        while now <= N:
            era[now] = 0
            now += i

start = 0
if len(prime_lst) > 1:
    end = 1
else: 
    end = 0
ans = 0
if prime_lst:
    ssum = prime_lst[start]
    if ssum == N:
        ans += 1

    while start < len(prime_lst):
        if ssum < N and end < len(prime_lst):
            ssum += prime_lst[end]
            end += 1
        else:
            ssum -= prime_lst[start]
            start += 1

        if ssum == N :
            ans += 1


print(ans)
