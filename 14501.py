# pypy3: 200ms
# 퇴사 D-N 
N = int(input())
Tis = []
Pis = []
for n in range(N):
    T, P = map(int, input().split())
    Tis.append(T)
    Pis.append(P)

def consulting(start, tot_earn):
    global mx_earn

    if start >= N:
        if mx_earn < tot_earn:
            mx_earn = tot_earn
        return

    if start + Tis[start] <= N:
        tot_earn += Pis[start]
    
    for next in range(min(N, start+Tis[start]), N+1):
        consulting(next, tot_earn)

mx_earn = 0
for i in range(0,N):
    consulting(i, 0)

print(mx_earn)