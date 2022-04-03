'''
python3: 128ms
pypy3: 164ms
'''
from collections import deque


def bfs(arr, start):
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        for i in range(4):
            new_r, new_c = now[0] + move[i][0], now[1] + move[i][1]
            if (new_r, new_c) != (0, 0) and new_r in range(N) and new_c in range(M):
                if arr[new_r][new_c] == 1:
                    arr[new_r][new_c] += arr[now[0]][now[1]]
                    queue.append((new_r, new_c))

                 
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int, input())))
    
bfs(arr, (0,0))
print(arr[-1][-1])
