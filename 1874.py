N = int(input())
stk = []
used = [0]*(N+1)
operate = []
making = []
wanted = []
for n in range(N):
    wanted.append(int(input()))
i = 1
pre = 0
for a in range(N):
    num = wanted[a]

    if num < pre:
        while 1:
            if stk:
                adding = stk.pop()
                operate.append('-')
                making.append(adding)
                if wanted[len(making)-1] != making[-1]:
                    print('NO')
                    exit()
                
                if adding == num:
                    break

            else:
                print('NO')
                exit()

    
    else:
        while i <= num:
            if not used[i]:
                stk.append(i)
                used[i] = 1
                operate.append('+')
                i += 1
        if a < N-1:
            if num < wanted[a+1]:
                adding = stk.pop()
                making.append(adding)
                operate.append('-')

        elif a == N-1 and stk:
            adding = stk.pop()
            making.append(adding)
            operate.append('-')

    pre = num


for op in operate:
    print(op)