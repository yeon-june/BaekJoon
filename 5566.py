import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [0] * N
for i in range(N):
    board[i] = int(input())

move = [0] * (M+1)
for k in range(1,M+1):
    move[k]  = int(input())


roll = [0] * (M+1)
roll[0] = 1
for j in range(1,M+1):
    roll[j] = move[j] + roll[j-1]
    if roll[j] >= N:
        ans = j
        break

    roll[j] = roll[j] + board[roll[j]-1]
    if roll[j] >= N:
        ans = j
        break



print(ans)