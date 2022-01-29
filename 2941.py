croatia_char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
length = len(word)
for char in croatia_char:
    length -= word.count(char)

print(length)