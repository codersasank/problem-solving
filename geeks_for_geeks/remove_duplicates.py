class Solution:
	def removeDups(self, s):
	    lst = list()
	    occurence = dict()
	    for ch in s:
	        if ch in occurence:
	            continue
	        lst.append(ch)
	        occurence[ch] = True
	    return "".join(lst)
