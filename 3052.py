mod_lst = []
for i in range(10):
    N = int(input())
    mod_lst.append(N % 42)

mod_set = set(mod_lst)
print(len(mod_set))