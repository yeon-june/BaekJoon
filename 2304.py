# 높이 값 유일 할 거라는 착각 금지

N = int(input())
# l(좌표)를 key로, h를 value로
sticks = dict()
# 좌표 오름차순 정렬용
stick_l = []
for n in range(N):
    l, h = map(int, input().split())
    sticks[l] = h
    stick_l.append(l)
stick_l.sort()

# 앞~ 첫번째 최대 높이/ 뒤~ 첫번째 최대 높이 인덱스
area = 0
#자기 좌표 이전 max height 저장용
stick_mh_b = sticks[stick_l[0]]
for i in range(0, N):
    # 첫번째 최대 높이 만나면 자기 넓이 저장후 break (앞~ 끝)
    if sticks[stick_l[i]] == max(sticks.values()):
        area += sticks[stick_l[i]]
        # 뒤~ process에서 멈출 index 값 저장
        first_max_index = i
        break
    
    # 자기 이전 최대 높이보다 자기 높이가 크면 자신의 높이값을 가짐, 아니면 이전의 높이 값 계승
    else:
        area += max(sticks[stick_l[i]], stick_mh_b) * (stick_l[i+1]- stick_l[i])
        stick_mh_b = max(sticks[stick_l[i]], stick_mh_b)

# 뒤~
stick_mh_b = sticks[stick_l[-1]]
for i in range(N-1, first_max_index, -1):
    area += max(sticks[stick_l[i]], stick_mh_b) * (stick_l[i]- stick_l[i-1])
    stick_mh_b = max(sticks[stick_l[i]], stick_mh_b)

print(area)