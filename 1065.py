def ishansoo(n):
    strn = str(n)
    if len(strn) in [1, 2]:
        return True
    
    dif = int(strn[0]) - int(strn[1])
    for i in range(len(strn)):
        try:
            dif1 = int(strn[i]) - int(strn[i+1])
        except:
            break
        if dif != dif1:
            return False
        dif = dif1
    
    return True

N = int(input())
count =0
for n in range(1, N+1):
    if ishansoo(n):
        count +=1

print(count)
