N = int(input())
num_lst = list(map(int,input().split()))
cur_max = -10000000
cur_min = 10000000
for num in num_lst:
    if num > cur_max:
        cur_max = num
    if num < cur_min:
        cur_min = num

print(cur_min, cur_max)
