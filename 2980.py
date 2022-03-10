N, L = map(int, input().split())
traffics = []
for n in range(N):
    D, R, G = map(int, input().split())
    traffics.append((D, R, G))
b_traffic = 0
sec = 0
for d, r, g in traffics:
    sec += d - b_traffic
    light = sec % (r + g)
    if light < r:
        sec += r - light
    b_traffic = d

sec += L - b_traffic
print(sec)