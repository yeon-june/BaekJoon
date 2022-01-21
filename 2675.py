T = int(input())

for t in range(T):
    r, s = input().split()
    r = int(r)
    s = str(s)
    for i in range(len(s)):
        print(r*s[i], end ='')
    print()