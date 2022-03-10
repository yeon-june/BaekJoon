N = int(input())
stk = []
for n in range(N):
    tmp = input()
    if tmp[:4] == 'push':
        com, num = tmp.split()
        num = int(num)
        stk.append(num)
    elif tmp == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)
    elif tmp == 'size':
        print(len(stk))
    elif tmp == 'empty':
        if stk:
            print(0)
        else:
            print(1)
    elif tmp == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)
