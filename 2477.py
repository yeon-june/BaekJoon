cham = int(input())
len_lst = []
ga_max =0
se_max =0
for i in range(6):
    N, length = map(int, input().split())
    if N > 2:
        if length > ga_max:
            ga_max = length
    else:
        if length > se_max:
            se_max = length
    len_lst.append(length)

# 제일 긴 변(가로/세로) 양 옆 변의 차이가 작은 사각형 (빠지는) 변 길이
if ga_max == se_max:
    si = len_lst.index(se_max)
    gi = len_lst.index(ga_max,si)
else:
    si = len_lst.index(se_max)
    gi = len_lst.index(ga_max)

whole = se_max * ga_max
sub = abs((len_lst[(si-1)%6]-len_lst[(si+1)%6]) * (len_lst[(gi-1)%6]-len_lst[(gi+1)%6]))


print(cham * (whole - sub))