S = input()
alphabets = []
for char in list(range(97, 123)):
        alphabets.append(S.find(chr(char)))


print(*alphabets)