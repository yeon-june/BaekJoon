# pypy3: 488ms

N = int(input())
time = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append((a,b))

time = sorted(time, key=lambda x:(x[1],x[0]))
print(time)
pre = time[0][1]
tot = 1
for i in range(1,N):
    if time[i][0] >= pre:
        tot += 1
        pre = time[i][1]

print(tot)


