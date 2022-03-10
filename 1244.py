N = int(input())
switch = list(map(int, input().split()))
S = int(input())
s_n = []
s_change = [1, 0]

for i in range(S):
    s, n = map(int, input().split())
    s_n.append([s, n])

for j in range(S):
    if s_n[j][0] == 1:
        for m in range(N):
            if not (m+1) % s_n[j][1]:
                switch[m] = s_change[switch[m]]


    else:
        change_idx =[s_n[j][1]-1]
        for k in range(1, min(N-s_n[j][1]+1 , s_n[j][1])):
            if switch[s_n[j][1]-1 - k] == switch[s_n[j][1]-1 + k]:
                change_idx.extend([s_n[j][1]-1 - k, s_n[j][1]-1 + k])
            else:
                break

        for idx in change_idx:
            switch[idx] = s_change[switch[idx]]


for idx in range(len(switch)):
    if idx !=0 and idx % 20 == 19:
        print(switch[idx])
    else:
        print(switch[idx], end = ' ')