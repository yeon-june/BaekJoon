A = int(input())
B = int(input())
C = int(input())

multi = str(A * B * C)

for i in range(10):
    cnt = multi.count(str(i))
    print(cnt)