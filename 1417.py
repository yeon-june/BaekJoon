N = int(input())
fir_v = int(input())
candidates = []
for i in range(N-1):
    candidates.append(int(input()))

cnt = 0
while candidates and fir_v <= max(candidates):
    for j in range(N-1):
        if candidates[j] == max(candidates):
            candidates[j] -= 1
            fir_v += 1
            cnt += 1
            break

print(cnt)

