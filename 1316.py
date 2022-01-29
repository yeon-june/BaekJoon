def isgroupword(word):
    for char in word:
        if not char*word.count(char) in word:
            return False
        
    return True
    
T = int(input())
count = 0
for t in range(T):
    if isgroupword(input()):
        count += 1

print(count)