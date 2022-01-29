N = int(input())
score_lst = list(map(int, input().split()))
max_score = max(score_lst)
new_score_lst = []
for score in score_lst:
    new_score_lst.append((score/max_score)*100)

s = 0
for new_score in new_score_lst:
    s += new_score

print(s/N)

