def LeftView(root):
    stack = [(root,0)]
    visited = dict()
    left_view = dict()
    max_lvl = 0
    while stack:
        top = stack[-1]
        if top[1]>max_lvl:
            max_lvl = top[1]
        if top[1] not in left_view:
            left_view[top[1]] = top[0]
        if top not in visited:
            if top[0].right is not None:
                stack.append( (top[0].right, top[1]+1) )
            if top[0].left is not None:
                stack.append((top[0].left, top[1]+1))
            visited[top] = True
        else:
            stack.pop(-1)
    
    ret = [left_view[i].data for i in range(max_lvl+1) ]
    return ret
