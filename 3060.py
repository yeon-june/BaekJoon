opposite = {0: 3, 1: 4, 2: 5, 3: 0, 4: 1, 5: 2}

T = int(input())
for t in range(T):
    N = int(input())
    feed = list(map(int, input().split()))
    day = 1
    ssum = sum(feed)
    while ssum <= N:
        ssum = 0
        b_feed = feed[::]
        for i in range(6):
            feed[i] = b_feed[(i-1) % 6] + b_feed[(i+1) % 6] + b_feed[opposite[i]] + b_feed[i]
            ssum += feed[i]

        day += 1

    print(day)