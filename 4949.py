brackets_start = ['[', '(']

sentence = input()
while sentence != '.':
    stk = []
    ans = 'yes'
    for char in sentence:
        if char in brackets_start:
            stk.append(char)
        
        elif char == ')':
            if stk:
                pre = stk.pop()
                if pre !='(':
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
        
        elif char == ']':
            if stk:
                pre = stk.pop()
                if pre != '[':
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
    
    if not stk:
        print(ans)
    else:
        print('no')
    
    sentence = input()