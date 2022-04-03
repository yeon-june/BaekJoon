'''
pypy3: 140ms
'''

N = int(input())
price = []
for n in range(N):
    price.append(list(map(int, input().split())))

painting = [[0] * 3 for _ in range(N)]
painting[0] = price[0]

for i in range(1, N):
    painting[i][0] = price[i][0] + min(painting[i-1][1], painting[i-1][2])
    painting[i][1] = price[i][1] + min(painting[i-1][0], painting[i-1][2])
    painting[i][2] = price[i][2] + min(painting[i-1][0], painting[i-1][1])

print(min(painting[N-1]))