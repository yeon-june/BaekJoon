# 인공지능 시계
time_h, time_m, time_s = map(int, input().split())
nt = int(input())
if time_s + nt >= 60:
    sec = (time_s + nt) % 60
    minute = time_m + (time_s + nt) // 60
    if minute >= 60:
        hour = time_h + minute//60
        minute =  minute % 60
        if hour >= 24:
            hour = hour % 24
        else: hour
    else:
        hour = time_h
else: 
    sec = time_s + nt
    minute = time_m
    hour = time_h

print('{} {} {}'.format(hour, minute, sec))
        