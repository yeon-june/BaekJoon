# input: 동서남북 / 위치

def location(direction, distance):
    # dxy = [방위, x, y] 
    if direction == 1:
        dxy = [direction, distance, 0]
    elif direction == 2:
        dxy = [direction,distance, h]    
    elif direction == 3:
        dxy = [direction,0, distance]
    else:
        dxy = [direction, w, distance]

    return dxy

w, h = map(int, input().split())
N = int(input())
stores =[]
for n in range(N):
    direction, distance = map(int, input().split())
    stores.append(location(direction, distance))

s_dir, s_dis = map(int, input().split())
security = location(s_dir, s_dis)

security_dis = 0
for store in stores:
    if store[0] == security[0]:
        security_dis += abs(store[1] - security[1] + store[2] - security[2])
    
    elif [store[0], security[0]] == [1,2] or [store[0], security[0]] == [2,1]:
        security_dis += h + min(w - store[1] + w - security[1], store[1] + security[1])
        
    elif [store[0], security[0]] == [3,4] or [store[0], security[0]] == [4,3]:
        security_dis += w + min(h - store[2] + h - security[2], store[2] + security[2])

    else:
        security_dis += abs(store[1]-security[1]) + abs(store[2]-security[2])

print(security_dis)