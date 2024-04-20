class Solution:
	def threeWayPartition(self, array, a, b):
	    less_a = 0 ; a_b = 0 ; grt_b = 0
	    for num in array:
	        if num<a:
	            less_a += 1
	        elif num>b:
	            grt_b += 1
	        else:
	            a_b += 1
	    idx_one = 0 ; idx_two = less_a ; idx_three = less_a + a_b
	    while idx_one < less_a:
	        if array[idx_one]<a:
	            idx_one += 1
	        elif array[idx_one]>b:
	            array[idx_one], array[idx_three] = array[idx_three], array[idx_one]
	            idx_three += 1
	        else:
	            array[idx_one], array[idx_two] = array[idx_two], array[idx_one]
	            idx_two += 1
	    while idx_two < less_a+a_b:
	        if array[idx_two]>b:
	            array[idx_two], array[idx_three] = array[idx_three], array[idx_two]
	            idx_three += 1
	        else:
	            idx_two += 1
	    return array
