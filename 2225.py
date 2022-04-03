# 합분해
# 중복조합 mHn = (m+n-1)Cn
# pypy3: 108ms
import math

N, M = map(int, input().split())
print((math.factorial(M+N-1)//(math.factorial(N) * math.factorial(M-1))) % 1000000000)