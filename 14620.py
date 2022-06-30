from itertools import combinations

def chk_cost(sx, sy):
    global min_cost
    global tmp

    for x,y in grow:
        tmp += bed[sx+x][sy+y]
        if tmp > min_cost:
            break


grow = [(0,1), (0,-1), (1,0), (-1,0), (0, 0)]
invalid = [(0,1), (1,0), (1,1), (2,0), (0,2)]
N = int(input())
bed = []
for _ in range(N):
    bed.append(list(map(int, input().split())))

points = [(i,j) for i in range(1,N-1) for j in range(1,N-1)]

three = list(combinations(points, 3))
min_cost = 10**10
for case in three:
    (x1, y1),(x2, y2),(x3,y3)= case
    a = (abs(x1-x2), abs(y1-y2))
    b = (abs(x1-x3), abs(y1-y3))
    c = (abs(x2-x3), abs(y2-y3))
    # 죽지 않게
    if a not in invalid and b not in invalid and c not in invalid:
        tmp = 0
        for point in case:
            chk_cost(point[0], point[1])

        if tmp < min_cost:
            min_cost = tmp


print(min_cost)