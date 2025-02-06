def matched(s):
    stack = list()
    brackets = ['(', ')']
    for ch in s:
        if ch not in brackets:
            continue
        if ch == '(':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                stack.pop(-1)
            else:
                return False
    if len(stack) == 0:
        return True
    return False
            
