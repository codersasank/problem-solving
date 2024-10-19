class Solution:
    def pageFaults(self, N, C, pages):
        used = [-1 for i in range(C)]
        memory = [None for i in range(C)]
        faults = 0
        for i in range(N):
            page = pages[i]
            try:
                idx = memory.index(page)
                used[idx] = i
            except:
                least_used = (0, used[0])
                for j in range(C):
                    if used[j]<least_used[1]:
                        least_used = (j, used[j])
                memory[least_used[0]] = page
                used[least_used[0]] = i
                faults += 1
        return faults
