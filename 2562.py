num_idx_dict = dict()
num_lst = []

for i in range(1,10):
    N = int(input())
    num_idx_dict[N] = i
    num_lst.append(N)

num_lst.sort()
print(num_lst[-1])
print(num_idx_dict[num_lst[-1]])

