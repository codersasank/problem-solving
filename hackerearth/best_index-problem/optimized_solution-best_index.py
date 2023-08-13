import math

def special_sum(idx, array, length, prev_last_element, prev_sum):
    spl_sum = 0

    remaining_length = length - idx 
    #print ("Remaining length for {0} is {1} ".format(idx,remaining_length))

    n = (math.sqrt(1+8*remaining_length)-1 )//2
    #print ("N for {0} is {1} ".format(idx,n))
    
    last_element = int ( (n*(n+1))/2 ) + idx-1 
    #print ("LE for {0} is {1} ".format(idx,last_element))
    
    if (prev_last_element==-1):
        for i in range(idx, last_element+1):
            spl_sum += array[i]
    else:
        if (prev_last_element==last_element):
            spl_sum = prev_sum - array[idx-1]
            
        if (prev_last_element>last_element):
            deduction = 0
            for j in range(prev_last_element, last_element, -1):
                deduction += array[j]
            spl_sum = prev_sum - deduction - array[idx-1]
            
        if (prev_last_element<last_element):
            addition = 0
            for j in range(prev_last_element+1, last_element+1):
                addition += array[j]
            spl_sum = prev_sum + addition - array[idx-1]    
            

    return (spl_sum, last_element)
    
array_len = int(input())
A = list( map(int, input().split()) )

max_spl_sum = -9223372036854775807
#n = (math.sqrt(1+8*5)-1 )//2
#print ("Calc:{0}".format(n))

prev_last_element = -1
prev_sum = 0

for i in range(0, array_len):
    spl_sum, prev_last_element = special_sum(i, A, array_len, prev_last_element, prev_sum)
    prev_sum = spl_sum
    if spl_sum > max_spl_sum:
        max_spl_sum = spl_sum
print(max_spl_sum)
