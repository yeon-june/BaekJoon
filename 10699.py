# 오늘 날짜

import datetime as dt
a = dt.datetime.now()

y = a.year
m = a.month
d = a.day

print('{}-{:02d}-{:2d}'.format(y, m, d))