def check(number):
    long = len(number)
    for k in range(2, long//2 + 1):
        if number[long-k:] == number[long-2*k:long-k]:
            return False

    return True

def dfs(now):
    if not check(now):
        return

    if len(now) == N:
        print(now)
        exit(0)

    for num in nums:
        if num != now[-1]:
            dfs(now+num)


N = int(input())
nums = ['1', '2', '3']
dfs('1')
