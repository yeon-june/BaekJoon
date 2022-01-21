# A+B-8
T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(t+1, a, b, a+b))