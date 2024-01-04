class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sat = 0
        g.sort()
        s.sort()
        g_n = len(g)
        s_n = len(s)
        g_p = 0
        c_p = 0
        while c_p<s_n and g_p<g_n:
            if s[c_p] >= g[g_p]:
                c_p += 1
                g_p += 1
                sat += 1
            else:
                c_p += 1
        return sat
