N = int(input())
brackets = list(map(str,input().split()))

used = [0]*10
mx_ans = ''
mn_ans = ''

def check(num1, num2, bracket):
    if bracket =='<':
        return num1 < num2
    else:
        return num1 > num2

def solution(idx, s):
    global mx_ans, mn_ans

    if(idx==N+1):
        if(len(mn_ans)==0):
            mn_ans = s
        else:
            mx_ans = s
        return

    for i in range(10):
        if not used[i]:
            if(idx==0 or check(s[-1], str(i), brackets[idx-1])):
                used[i]=True
                solution(idx+1, s + str(i))
                used[i]=False


solution(0,'')
print(mx_ans)
print(mn_ans)