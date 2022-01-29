a, b = input().split()
a_rev = int(a[::-1])
b_rev = int(b[::-1])

if a_rev > b_rev:
    print(a_rev)
else:
    print(b_rev)
