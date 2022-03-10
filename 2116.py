# 주사위 반대 인덱스 지정
def index_opposite(idx):
    if idx == 0:
        return 5
    if idx == 1:
        return 3
    if idx == 2:
        return 4
    if idx == 3:
        return 1
    if idx == 4:
        return 2
    if idx == 5:
        return 0   


# 입력값 받기
N = int(input())
dice =[]

# 주사위 받기 
for n in range(N):
    die = list(map(int, input().split()))
    dice.append(die)


side_sum_max = 0
# 처음 윗면의 값에 따른 상황별 최대값 구하기, 최대값 갱신
# i: 맨 처음 주사위의 윗면
for i in range(1,7):
    side_sum = 0
    top = i
    # j 주사위 index (dice내의 각 주사위 index)
    for j in range(N):
        # 이전 주사위 윗면의 인덱스 (각 주사위의 면 인덱스)
        idx = dice[j].index(top)
        opposite = index_opposite(idx)
        # 현재 쌓을 주사위의 윗면 갱신
        top= dice[j][opposite]
        # 사이드 값 처리를 위한 주사위 복사
        replicated_dice = dice[j][::]
        # 앞 인덱스 값 유지하면서 top, bottom 값 주사위에서 제거
        del replicated_dice[max(idx,opposite)]
        del replicated_dice[min(idx,opposite)]
        # 사이드 중 가장 큰 값 더하기
        side_sum += max(replicated_dice)
    # 상황별 max값 갱신
    if side_sum_max < side_sum:
        side_sum_max = side_sum

print(side_sum_max)
