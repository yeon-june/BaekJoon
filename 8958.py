T = int(input())

for t in range(T):
    ox = input()
    score = 0
    tot_score = 0
    for char in ox:
        if char == 'O':
            score += 1
            tot_score += score
        else:
            score = 0
    print(tot_score)