# 수열은 증가, 감소의 2가지 경우가 있음
# 함께 보기 어려우니 경우를 나늠

# 증가 경우 최대 길이
def increasing_len(lst):
    max_len= 0
    cnt = 1
    for i in range(len(lst)-1):
        if lst[i] <= lst[i+1]:
            cnt += 1
        
        else:
            if max_len < cnt:
                max_len = cnt
            cnt = 1
    if max_len < cnt:
        max_len = cnt
    return max_len

# 감소 경우 최대 길이
def decreasing_len(lst):
    max_len= 0
    cnt = 1
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            cnt +=1
        
        else:
            if max_len < cnt:
                max_len = cnt
            cnt = 1
    if max_len < cnt:
        max_len = cnt
    return max_len


N = int(input())
num_lst = list(map(int, input().split()))
# 증가, 감소 중 최대를 골라 print
print(max(increasing_len(num_lst), decreasing_len(num_lst)))
        