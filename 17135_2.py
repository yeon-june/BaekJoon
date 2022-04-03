'''
pypy3: 236ms
python3: 604ms
'''

from itertools import combinations

# 거리 계산
def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

# 공격
def attack():
    tmp = []
    for ar_col in case:
        min_dis = 1000
        closest = 0
        # 열 우선 (왼쪽 먼저)
        for j in range(M):
            for i in range(ar_row - 1, -1, -1):
                # 공격할 적 판단
                if simul_board[i][j] == 1:
                    dis = distance(ar_row, ar_col, i, j)
                    if dis <= D and dis < min_dis:
                        min_dis = dis
                        closest =(i,j)
        # 공격할 적이 있다면 리스트에 추가
        if closest:
            tmp.append(closest)
    # 이번 턴 제거 적 리스트 반환
    return tmp


N, M, D = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))

col_n = list(range(M))
archer_combi = combinations(col_n, 3)

# 궁수 위치에 따라 시뮬레이션
mx_attack = 0
for case in archer_combi:
    simul_attack = 0
    # 복사
    simul_board = [row[:] for row in arr]
    # 궁수 움직이기 (각 턴마다 적이 움직이는 걸 반대로)
    for ar_row in range(N, 0, -1):
        # 공격
        attacked = attack()

        # 공격한 적 제거
        for enemy in attacked:
            if simul_board[enemy[0]][enemy[1]] == 1:
                simul_board[enemy[0]][enemy[1]] = 0
                simul_attack += 1
    # 한 시뮬레이션 결과 최종 비교
    if simul_attack > mx_attack:
        mx_attack = simul_attack


print(mx_attack)