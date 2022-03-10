# pop + insert 시간복잡도 위험 너무 높음!
def gear_turn(gear, d):
    if d == 1:
        tmp = gear.pop()
        gear.insert(0,tmp)               
      
    else:
        tmp = gear.pop(0)
        gear.insert(7,tmp)

    return gear

def check_left(g, d):
    if g < 0:
        return
    if gears[g][2] != gears[g+1][6]:
        check_left(g-1,d*(-1))
        gears[g].rotate(d)

def check_right(g, d):
    if g > 3:
        return
    if gears[g-1][2] != gears[g][6]:
        check_right(g+1,d*(-1))
        gears[g].rotate(d)


import collections
gears = []
for _ in range(4):
    gears.append(collections.deque(input()))
print(gears)

K = int(input())
turns = []
for k in range(K):
    g, d = map(int, input().split())
    turns.append((g,d))

for i in range(K):
    g = turns[i][0] -1
    d = turns[i][1]

    check_left(g-1, d*(-1))
    check_right(g+1, d*(-1))
    gears[g].rotate(d)

answer = int(gears[0][0])*1 + int(gears[1][0])*2 + int(gears[2][0])*4 + int(gears[3][0])*8

print(answer)

