def factorization(num):
    fac_lst = []
    for i in range(2, int(num**0.5)+1):
        while not num % i:
            num //= i
            fac_lst.append(i)

    if num != 1:
        fac_lst.append(num)

    return fac_lst

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

C = A1*B2 + A2*B1 # 분자
D = B1*B2 # 분모

c_factorize = factorization(C)
d_factorize = factorization(D)

del_lst = []
for n in c_factorize:
    if n in d_factorize:
        del_lst.append(n)
        d_factorize.remove(n)

for some in del_lst:
    c_factorize.remove(some)

ans1 = 1
for c in c_factorize:
    ans1 *= c

ans2 = 1
for d in d_factorize:
    ans2 *= d

print(ans1, ans2)