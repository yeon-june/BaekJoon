def d(n):
    self_tot = 0
    for num in str(n):
        self_tot += int(num)
    return n + self_tot

'''for i in range(1, 10001):
    sn =True
    for num in range(1, i+1):
        if d(num) == i:
            sn = False
            break
    if sn:
        print(i)'''

numbers_set = set(range(1, 10001))
remove_set = set()
for num in numbers_set:
    if d(num) <= 10000:
        remove_set.add(d(num))

print_num = list(numbers_set - remove_set)
print_num.sort()
for n in print_num:
    print(n)


