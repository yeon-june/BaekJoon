T = int(input())
for t in range(T):
    N = int(input())
    numbers = [input() for _ in range(N)]
    numbers.sort()
    # numbers = ['113', '12340', '123440', '12345', '98346']

    flag = True
    for i in range(N-1):
        length = len(numbers[i])
        if numbers[i] == numbers[i+1][:length]:  #앞뒤만 확인하면 되는 이유: 시작 번호가 다르면 애초에 가능성이 없음
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')

