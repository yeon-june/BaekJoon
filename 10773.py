N = int(input())
stk = []
for n in range(N):
    num = int(input())
    if num == 0:
        if stk:
            stk.pop()
    else:
        stk.append(num)

print(sum(stk))