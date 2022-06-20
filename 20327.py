def first(l, arr):
    length = 2**N//2**l
    tot = length**2
    tmp = [row[:] for row in arr]
    for i in range(tot):
        for j in range(tot):
            r = (i % length) * 2**l
            c = (j % length) * 2**l
            for n in range(r, r+2**l):
                for m in range(c, c+2**l):
                    tmp[n][m] = arr[2**l-1-(n-r)][m]

def second(l, arr):
    length = 2**N//2**l
    tot = length**2
    tmp = [row[:] for row in arr]
    for i in range(tot):
        for j in range(tot):
            r = (i % length) * 2**l
            c = (j % length) * 2**l
            for n in range(r, r+2**l):
                for m in range(c, c+2**l):
                    tmp[n][m] = arr[n][2**l-1-(m-c)]

def third(l, arr):
    length = 2**N//2**l
    tot = length**2
    tmp = [row[:] for row in arr]
    for i in range(tot):
        for j in range(tot):
            r = (i % length) * 2**l
            c = (j % length) * 2**l
            for n in range(r, r+2**l):
                for m in range(c, c+2**l):
                    tmp[m][r+2**l-n-1+r] = arr[n][m]



N, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]

for _ in range(R):
    cal, l = map(int, input())

