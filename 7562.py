'''
pypy3: 408ms
python3: 시간초과
'''

from collections import deque


moves = [(-1,2), (1,2), (-2,1), (2,1), (-2,-1), (2,-1), (-1,-2), (1,-2)]
def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        now_c = board[now[1]][now[0]]
        print(now_c)
        if now == end:
            return

        for move in moves:
            n_w, n_h = now[0] + move[0], now[1] + move[1]
            if n_w in range(I) and n_h in range(I) and board[n_h][n_w] == 0:
                queue.append([n_w,n_h])
                board[n_h][n_w] = now_c + 1
    



T = int(input())
for t in range(T):
    I = int(input())
    board = [[0] * I for _ in range(I)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    bfs(start)
    print(board[end[0]][end[1]])
    

