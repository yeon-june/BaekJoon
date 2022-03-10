N, K = map(int, input().split())
wheel = ['?'] * N
spins = []
for k in range(K):
    spins.append(list(input().split()))

idx = 0
for spin in spins:
    if wheel[(idx - int(spin[0])) % N] == '?':
        wheel[(idx - int(spin[0])) % N] = spin[1]
        idx = (idx - int(spin[0])) % N
    elif wheel[(idx - int(spin[0])) % N] == spin[1]:
        idx = (idx - int(spin[0])) % N
    else:
        print('!')
        exit()


unknown =  wheel.count('?')
if unknown > 0 and len(wheel) - unknown + 1  != len(set(wheel)):
    print('!')
elif unknown == 0 and len(wheel) != len(set(wheel)):
    print('!')
else:
    ans = wheel[idx:] + wheel[:idx]
    print(''.join(ans))

