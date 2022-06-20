# N-Queen
# pypy3: 30748ms

N = int(input())

ans = 0
row = [0] * N

def promising(x):
    for i in range(x): # 이전 줄 까지만 보겠다
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return 0

    return 1

def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return

    else:
        for i in range(N):
            row[x] = i
            if promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
