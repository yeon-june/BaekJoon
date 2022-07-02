import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
calc = list(map(int, input().split()))

mx_calc = -10**10
mn_calc =10**10

def dfs(sym_info, i, num):
    global mx_calc
    global mn_calc
    
    if i == N:
        if num > mx_calc:
            mx_calc = num
        if num < mn_calc:
            mn_calc = num
        return

    for a in range(4):
        if sym_info[a]:
            sym_info[a] -= 1
            if a==0:
                dfs(sym_info[:], i+1, num + A[i])
            elif  a==1:
                dfs(sym_info[:], i+1, num - A[i])
            elif  a==2:
                dfs(sym_info[:], i+1, num * A[i])
            else:
                dfs(sym_info[:], i+1, int(num / A[i]))  

            sym_info[a] += 1

dfs(calc,1,A[0])

print(mx_calc)
print(mn_calc)



