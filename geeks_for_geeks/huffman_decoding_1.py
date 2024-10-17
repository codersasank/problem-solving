class Solution:
    def decode_file(self, root: MinHeapNode, s: str):
        n = len(s)
        ret = list()
        cur = root
        for i in range(n):
            if cur.data!="$":
                ret.append(cur.data)
                cur = root
            if s[i]=="0":
                cur = cur.left
            else:
                cur = cur.right
        if cur.data!="$":
            ret.append(cur.data)
        #if len(ret)==1:
        #    return ""
        return "".join(ret)
