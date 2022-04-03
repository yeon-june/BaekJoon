N = int(input())
for n in range(N):
    brackets = input()
    stk = []
    stop = 0
    for b in brackets:
        if b == '(':
            stk.append(b)
        else:
            if stk:
                pre = stk.pop()
                if pre != '(':
                    print('NO')
                    stop = 1
                    break
            else:
                print('NO')
                stop = 1
                break
    if not stk and not stop:
        print('YES')
    elif not stop:
        print('NO')