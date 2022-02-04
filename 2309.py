dwarf = []
# 키 저장
for i in range(9):
    dwarf.append(int(input()))

# 전체에서 100을 뺀 2명 키의 합
two_height = sum(dwarf) - 100

# 가능한 2명 조합
combi = []
for a in dwarf:
    for b in dwarf:
        if a != b:
            combi.append([a, b])

# 2명 조합중, 100을 만들수 있는 2명 조합(2명 뺐을 때 100) 찾기, 지우기
for [A, B] in combi:
    if A + B == two_height:
        dwarf.remove(A)
        dwarf.remove(B)
        break

# 정렬 후 출력
dwarf.sort()
for d in dwarf:
    print(d)

