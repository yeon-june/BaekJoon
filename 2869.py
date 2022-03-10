A, B, V = map(int, input().split())
day = (V-B) / (A-B)
if (V-B) % (A-B):
    print(int(day+1))
else:
    print(int(day))