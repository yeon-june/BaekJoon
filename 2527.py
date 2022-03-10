# 사각형의 x, y 좌표 모음 (각각)
def included_xy(rectangle):
    xy_range = [0,0]
    xy_range[0] = set(range(rectangle[0],rectangle[2]+1))
    xy_range[1] = set(range(rectangle[1],rectangle[3]+1))

    return xy_range
    

for i in range(4):
    lst = list(map(int,input().split()))
    r1 = lst[:4]
    r2 = lst[4:]
    r1_range = included_xy(r1)
    r2_range = included_xy(r2)
    # r1, r2의 x, y 교집합 찾기
    inter_x = r1_range[0] & r2_range[0]
    inter_y = r1_range[1] & r2_range[1]

    # x, y 모두 겹치지 않을 때
    if not (inter_x and inter_y):
        print('d')
    
    # x, y 모두 2개 이상 겹칠 때 (사각형)
    elif len(inter_x) > 1 and len(inter_y) > 1:
        print('a')
    
    # x, y 중 1개, 나머지는 2개 이상 겹칠 때 (선)
    elif (len(inter_x) == 1 and len(inter_y) > 1) or (len(inter_x) > 1 and len(inter_y) ==1):
        print('b')
    
    # 나머지 (점)
    else:
        print('c')

    
