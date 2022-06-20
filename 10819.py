from itertools import permutations

def calculate(numbers):
    tot = 0
    for i in range(N-1):
        tot += abs(numbers[i]-numbers[i+1])
    return tot


N = int(input())
numbers = list(map(int, input().split()))
listings = permutations(numbers, N)

res = 0
for li in listings:
    test = calculate(li)
    if test > res:
        res = test

print(res)
