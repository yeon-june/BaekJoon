word = input().upper()

max_count = 0 
count_lst = []
for char in set(list(word)):
    count_lst.append(word.count(char))
    if word.count(char) > max_count:
        max_count = word.count(char)
        max_char = char

if count_lst.count(max_count) >= 2:
    print('?')
else:
    print(max_char)
    
