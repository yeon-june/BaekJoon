# 오븐 시계
time_h , time_m = map(int, input().split())
need_t = int(input())
if time_m + need_t >= 60:
    minute = (time_m + need_t)%60
    hour = time_h + (time_m + need_t)//60
    if hour >= 24:
        hour -= 24
else:
    minute = time_m + need_t
    hour = time_h

print('{} {}'.format(hour, minute))