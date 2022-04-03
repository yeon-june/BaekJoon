from collections import deque

# 현재가 대각일 때 movement
d_move = [(1, 0, 'H'), (1, 1, 'D'), (0, 1, 'V')]
# 현재가 가로일 때 movement
h_move = [(1, 0, 'H'), (1, 1, 'D')]
# 현재가 세로일 때 movement
v_move = [(1, 1, 'D'), (0, 1, 'V')]


def bfs(end, arr):
    global cnt
    queue = deque()
    queue.append(end)

    while queue:
        now = queue.popleft()
        if now[0] == N-1 and now[1] == N-1:
            cnt += 1

        else:
            new_start = (now[0], now[1])

            if now[2] == 'H':
                for move in h_move:
                    new_end = (new_start[0] + move[0], new_start[1] + move[1], move[2])
                    if move[2] == 'H' and new_end[0] in range(N) and new_end[1] in range(N) and arr[new_end[1]][new_end[0]] == 0:
                        queue.append(new_end)

                    elif move[2] == 'D' and new_end[0] in range(N) and new_end[1] in range(N) and arr[new_end[1]][new_end[0]]==0 and arr[new_end[1]-1][new_end[0]] == 0 and arr[new_end[1]][new_end[0]-1] == 0:
                        queue.append(new_end)

            elif now[2] == 'D':
                for move in d_move:
                    new_end = (new_start[0] + move[0], new_start[1] + move[1], move[2])
                    if (move[2] in ['H', 'V']) and new_end[0] in range(N) and new_end[1] in range(N) and arr[new_end[1]][new_end[0]] == 0:
                        queue.append(new_end)

                    elif move[2] == 'D' and new_end[0] in range(N) and new_end[1] in range(N) and arr[new_end[1]][new_end[0]] == 0 and arr[new_end[1]-1][new_end[0]] == 0 and arr[new_end[1]][new_end[0]-1] == 0:
                        queue.append(new_end)

            elif now[2] == 'V':
                for move in v_move:
                    new_end = (new_start[0] + move[0], new_start[1] + move[1], move[2])
                    if move[2] == 'V' and new_end[0] in range(N) and new_end[1] in range(N) and arr[new_end[1]][new_end[0]] == 0:
                        queue.append(new_end)

                    elif move[2] == 'D' and new_end[0] in range(N) and new_end[1] in range(N) and arr[new_end[1]][new_end[0]] == 0 and arr[new_end[1]-1][new_end[0]] == 0 and arr[new_end[1]][new_end[0]-1] == 0:
                        queue.append(new_end)




N = int(input())
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))

end = (1, 0, 'H')
cnt = 0

if arr[0][2] == 1 or (arr[N-1][N-2] == 1 and arr[N-2][N-1]) == 1:
    print(0)
elif arr[-1][-1]:
    print(0)

else:
    bfs(end, arr)
    print(cnt)
