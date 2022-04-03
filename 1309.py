'''
python3: 198ms
N = int(input())
cage = [[0]*3 for _ in range(N)]
# 0, 왼, 오
cage[0] = [1, 1, 1]
for i in range(1, N):
    cage[i] = [(cage[i-1][0] + cage[i-1][1] + cage[i-1][2]) % 9901, (cage[i-1][0] + cage[i-1][2]) % 9901, (cage[i-1][0] + cage[i-1][1]) % 9901]

print(sum(cage[N-1]) % 9901)
'''
# python3: 136ms
# pypy3: 112ms

N = int(input())
# 배치 x, 왼, 오 
# idx = 0 이전 상태 idx =1 지금 상태
cage = [[1, 1, 1], [0, 0, 0]]
if N == 1:
    print(sum(cage[0]))
else:
    for _ in range(1, N):
        cage[1] =  [(cage[0][0] + cage[0][1] + cage[0][2]) % 9901, (cage[0][0] + cage[0][2]) % 9901, (cage[0][0] + cage[0][1]) % 9901]
        cage[0] = cage[1]


    print(sum(cage[1]) % 9901)

# print(sum(cage[0]) % 9901) 이면 if 문 안걸고 가능
