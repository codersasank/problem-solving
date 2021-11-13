def num_consecutive_hashes(binary):
    cnt = 0
    while (binary!=0):
        binary = (binary & (binary << 1))
        cnt += 1
    return cnt

def calc_maximum_border_2(array, n, m, mode):
    max_consecutive = -10000

    if (mode=="UP"):
        direction = -1
        rows = n
        columns = m
        start = 0
    elif (mode=="DOWN"):
        direction = +1
        rows = n
        columns = m
        start = n-1
    elif (mode=="LEFT"):
        direction = -1
        rows = m
        columns = n
        start = 0
    elif (mode=="RIGHT"):
        direction = +1
        rows = m
        columns = n
        start = m-1

    for j in range(rows):
        if j==start:
            hash_count = num_consecutive_hashes(array[j])
            if hash_count > max_consecutive:
                max_consecutive = hash_count
            continue
        else:
            #print ("J:{0}, Mode:{1}".format(j,mode))
            if mode=="UP" or mode=="LEFT":
                hashes = array[j] & (~array[j-1])
                hash_count = num_consecutive_hashes(hashes)
                if hash_count > max_consecutive:
                    max_consecutive = hash_count
                continue
                
            else:
                hashes = array[j] & (~array[j+1])
                hash_count = num_consecutive_hashes(hashes)
                if hash_count > max_consecutive:
                    max_consecutive = hash_count
                continue
            
    return max_consecutive

num_of_test_cases = int(input())


for i in range(num_of_test_cases):
    array = []
    t_array_temp = []
    t_array = []
    n, m = [int(i) for i in input().split()]
    for j in range(n):
        row_str = input()
        row_str = row_str.replace('.','0')
        row_str = row_str.replace('#','1')
        t_array_temp.append(row_str)
        row = int(row_str, 2)
        array.append(row)
    #print (t_array_temp)
    for j in range(m):
        col_str = ""
        for i in range(n):
            #print ("J: {0}, I: {1}".format(j,i))
            col_str += t_array_temp[i][j]
        column = int(col_str, 2)
        t_array.append(column)

    print ( max ( calc_maximum_border_2(t_array,n,m,"LEFT"), calc_maximum_border_2(t_array,n,m,"RIGHT"), calc_maximum_border_2(array,n,m,"UP"), calc_maximum_border_2(array,n,m,"DOWN")  ) )    
