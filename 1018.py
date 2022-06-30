import sys
input = sys.stdin.readline

min_change = 64
valid = [[['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],],
         [['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],]
        ]

def check(sr, sc):
    global min_change
    for v in valid:
        tmp = 0
        for r in range(8):
            for c in range(8):
                if v[r][c] != board[sr+r][sc+c]:
                    tmp += 1
                
                if tmp >= min_change:
                    break

        if tmp < min_change:
            min_change = tmp


N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

for i in range(N-7):
    for j in range(M-7):
        check(i,j)

print(min_change)