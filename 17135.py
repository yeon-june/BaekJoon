from itertools import combinations


def turn(simul_attack, t):
    # attack
    tmp = []
    for archer in ars:
        reach = 10**10
        for enemy in s_enemies:
            if enemy[0]+t-1 < N-D:
                break

            if enemy not in removed:
                dis = abs(archer[0]-enemy[0]-t+1) + abs(archer[1]-enemy[1]) 
                if dis == 1:
                    reach = dis
                    closest = enemy
                    break
                
                elif dis < reach:
                    reach = dis
                    closest = enemy

        if reach <= D:
            if closest not in tmp:
                tmp.append(closest)

    simul_attack += len(tmp)
    removed.extend(tmp)
    
    # 적 움직임
    for enemy in s_enemies:
        if enemy not in removed:
            if enemy[0] + t == N:
                removed.append(enemy)
    
    return simul_attack


N, M, D = map(int, input().split())
arr = []
enemies = []
for n in range(N):
    arr.append(list(map(int, input().split())))


for i in range(N-1, -1, -1):
    for j in range(M):
        if arr[i][j] == 1:
            enemies.append([i,j])

if len(enemies)== N*M:
    print(3*N)

else:
    tot_enemies = len(enemies)
    mx_attack = 0
    col_n = list(range(M))
    archer_combi = combinations(col_n, 3)
    for combi in archer_combi:
        simul_attack = 0
        removed = []
        s_enemies = [enemy[:] for enemy in enemies]
        ars = [[N, combi[0]], [N, combi[1]], [N, combi[2]]]
        t = 0

        while len(removed) < tot_enemies:
            t += 1
            simul_attack = turn(simul_attack, t)

            if tot_enemies - len(removed) + simul_attack < mx_attack:
                break


        if simul_attack > mx_attack:
            mx_attack = simul_attack

        if mx_attack == tot_enemies:
            break

    print(mx_attack)
