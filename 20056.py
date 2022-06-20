# 마법사 상어와 파이어볼
# pypy3: 328ms
'''
파이어볼 이동 명령
1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
   (이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.)
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
   2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
   2-2. 파이어볼은 4개의 파이어볼로 나누어진다.
   2-3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        질량은 "(합쳐진 파이어볼 질량의 합)/5"이다.
        속력은 "(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)"이다.
        합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
   2-4. 질량이 0인 파이어볼은 소멸되어 없어진다.
'''
move = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
N, M, K = map(int, input().split())
fireball = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([(r,c), m, s, d])

for k in range(K):
    # 이동, 모으기
    moved_fireball = dict()
    for fire in fireball:
        n_r, n_c = (fire[0][0] + move[fire[3]][0]*fire[2])%N, (fire[0][1] + move[fire[3]][1]*fire[2])%N
        if (n_r, n_c) not in moved_fireball.keys():
            moved_fireball[(n_r, n_c)] = [fire[1], fire[2] ,fire[3], 1]
        else:
            cur =moved_fireball[(n_r, n_c)]
            if cur[2] == 'odd':
                n_d = 'odd'
            elif cur[2] % 2 != fire[3] % 2:
                n_d = 'odd'
            else:
                n_d = cur[2]

            moved_fireball[(n_r, n_c)] = [cur[0]+fire[1], cur[1]+fire[2], n_d, cur[3]+1]

    fireball = []
    # 2개 이상 모인 파이어볼 나누기
    for loc, info in moved_fireball.items():
        if info[3] == 1:
            fireball.append([loc, info[0], info[1], info[2]])
        else:
            if info[2] == 'odd' and info[0]//5:
                for i in range(1, 8, 2):
                    fireball.append([loc, info[0]//5, info[1]//info[3], i])
            elif info[2] != 'odd' and info[0]//5:
                for i in range(0, 7, 2):
                    fireball.append([loc, info[0]//5, info[1]//info[3], i])

tot = 0
for f in fireball:
    tot += f[1]

print(tot)