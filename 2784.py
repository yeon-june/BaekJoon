from itertools import permutations

words = [0] * 6
for i in range(6):
    words[i] = list(input())

three = list(map(list,permutations(words,3)))

ans = 0
for case in three:
    flag = 1
    others = words[:]
    for word in case:
        others.remove(word)

    rev_case = list(map(list, zip(*case)))
    for w in others:
        if w in rev_case:
            rev_case.remove(w)
        else:
            flag=0
            break

    if flag:
        ans = case
        break


if ans:
    for row in ans:
        print(''.join(row))
else:
    print(0)