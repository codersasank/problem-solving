class Solution:
    def smallestSubstring(self, S):
        freq = [0, 0, 0]
        for ch in S:
            freq[int(ch)] += 1
        n = freq[0] + freq[1] + freq[2]
        left = 0 ; right = -1
        if not (freq[0]>=1 and freq[1]>=1 and freq[2]>=1):
            return -1
        min_length = n ; freq = [0, 0, 0]
        for left in range(n):
            #print ( left, right )
            if (freq[0]<1 or freq[1]<1 or freq[2]<1) and right==n-1:
                break
            while (freq[0]<1 or freq[1]<1 or freq[2]<1) and right<n-1:
                right += 1
                freq[int(S[right])] += 1
                #print ( freq )
            substring_length = right-left+1
            min_length = min(substring_length, min_length)
            freq[int(S[left])] -= 1
        return min_length
            
            
