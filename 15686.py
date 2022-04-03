'''
풀이: 40분
python3: 344ms
pypy3: 176ms
'''
from itertools import combinations

N, M = map(int, input().split())
arr = []
chicken = []
house = []
# 문제 정보 받기
for n in range(N):
    arr.append(list(map(int, input().split())))
    for i in range(N):
        if arr[n][i] == 2:
            chicken.append((n,i))
        elif arr[n][i] == 1:
            house.append((n,i))
tot_chick = len(chicken)

# 가게 폐업 시뮬레이션
def chicken_simul(rm_set, simul):
    # 이전 시뮬레이션보다 결과가 안좋으면 바로 끝내기
    global town_ch_dis
    tot_dis = 0
    simul = simul - rm_set
    # 하우스마다 치킨집까지 최소 거리 구해서 시뮬 최종 결과 구하기
    for h in house:
        min_dis = 10**8
        for chick in simul:
            dis = abs(chick[0]-h[0]) + abs(chick[1]-h[1])
            if dis < min_dis:
                min_dis = dis

        tot_dis += min_dis
        # 이전 시뮬레이션이랑 비교 -> 없어져도 큰 차이 없음 176ms -> 184ms (케이스가 아주 크지 않아서 그런듯)
        if tot_dis >= town_ch_dis:
            return 10**10
    
    return tot_dis
    

# 폐업 가능 조합
candidates = combinations(chicken,tot_chick - M)
# 초기값
town_ch_dis = 10**10
for can in candidates:
    simul = set(chicken)
    rm_lst = set(can)
    simul_r = chicken_simul(rm_lst, simul)
    if simul_r < town_ch_dis:
        town_ch_dis = simul_r

print(town_ch_dis)


