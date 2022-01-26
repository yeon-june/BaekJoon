N, X = map(int, input().split())
lst = list(map(int, input().split()))
l_lst = []
for i in range(N):
    if lst[i] <  X:
        l_lst.append(str(lst[i]))

print(' '.join(l_lst))
    