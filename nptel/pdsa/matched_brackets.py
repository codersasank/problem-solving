def matched(s):
    stack = list()
    brackets = ['(', ')']
    for ch in s:
        if ch not in brackets:
            continue
        if ch == '(':
            stack.append(ch)
        else:
            if (not stack) or stack[-1] != '(':
                return False
            else:
                stack.pop(-1)
    if len(stack) == 0:
        return True
    return False
            
