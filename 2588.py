a = int(input())
b = int(input())

one_num = b%10
ten_num = int((b%100 - one_num)/10)
hun_num = b//100

print(one_num, ten_num, hun_num)


print(a*one_num)
print(a*ten_num)
print(a*hun_num)
print(a*b)
