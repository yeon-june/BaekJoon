# 마법사 상어와 토네이도
# pypy3: 324ms

directions = [(0,-1), (1,0), (0,1), (-1,0)]
# 모래 이동
ratio = [ 
[(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1), (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 1)]
]
ratio += [[(-y, x, z) for x, y, z in ratio[0]]]
ratio += [[(x, -y, z) for x, y, z in ratio[0]]]
ratio += [[(y, x, z) for x, y, z in ratio[0]]]

# 배열 내 움직임
def move(cur_r, cur_c):
    d = 0
    while cur_r != 0 or cur_c != 0:
        new_r, new_c = cur_r + directions[d][0], cur_c + directions[d][1]

        if not visited[new_r][new_c]:
            visited[new_r][new_c] = 1
            cur_r, cur_c = new_r, new_c
            storm((cur_r, cur_c), d)
            d = (d+1) % 4

        else:
            d = (d-1) % 4


# 모래날리기
def storm(start, direct):
    global ans
    tmp = 0
    for r, c, rat in ratio[direct]:
        if rat == 1:
            sand_mv = sand[start[0]][start[1]] - tmp
        else:
            sand_mv = int(sand[start[0]][start[1]] * rat)
            tmp += sand_mv
        
        t_r, t_c = start[0] + r, start[1] + c
        if t_r in range(N) and t_c in range(N):
            sand[t_r][t_c] += sand_mv
        else:
            ans += sand_mv

    sand[start[0]][start[1]] = 0


ans = 0
N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
start = (N//2, N//2)
visited[start[0]][start[1]] = 1

move(start[0], start[1])
print(ans)