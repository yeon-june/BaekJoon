a, b, c = map(int, input().split())

if a==b==c:
    print(10000+1000*a)
    exit()
elif a==b:
    print(1000 + 100*a)
    exit()
elif b==c:
    print(1000 + 100*b)
    exit()
elif c==a:
    print(1000 + 100*c)
    exit()
elif a!=b and b!=c and a!=c:
    print(max(a,b,c)*100)
    exit()
