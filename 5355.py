#  @ 3 곱하기
#  % 5 더하기
#  # 7 빼기

T = int(input())

for t in range(T):
    cal = list(input().split())
    num = float(cal[0])
    for i in range(len(cal)):
        if cal[i] == '@':
            num *= 3
        elif cal[i] == '%':
            num += 5
        elif cal[i] == '#':
            num -= 7

    print('{:.2f}'.format(num))