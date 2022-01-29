T = int(input())

for t in range(T):
    scores = list(map(int,input().split()))
    N = scores.pop(0)
    tot = sum(scores)
    average = tot/N
    above_avg = 0
    for score in scores:
        if score > average:
            above_avg += 1
    percentage = (above_avg/N)*100
    print(f'{percentage:0.3f}%')
