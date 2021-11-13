def get_cell(array, row, column, mode):
    if mode=="UP" or mode=="DOWN":
        return array[row][column]
    else:
        return array[column][row]

def calc_maximum_border(array, n, m, mode):
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

    #print ("rows: {0}, columns: {1}".format(rows,columns))

    if True:
        #for j in range(n):
        for j in range(rows):
            consec_list = []
            hash_count = 0
            count = False

            #if j==0:
            if j==start:
                #for i in range(m):
                for i in range(columns):
                    #print ("{0}, {1}, {2}".format(i,j, mode))
                    if (get_cell(array,j,i,mode)=="#") and not count:
                        count = True
                        hash_count += 1
                    elif (get_cell(array,j,i,mode)=="#") and count:
                        hash_count += 1
                    elif (get_cell(array,j,i,mode)==".") and count:
                        consec_list.append(hash_count)
                        hash_count = 0
                        count = False
                if count and hash_count>0:
                    consec_list.append(hash_count)
                    hash_count = 0
                    count = False
                if consec_list:
                    if max(consec_list)>max_consecutive:
                        max_consecutive = max(consec_list)
                continue

            else:
                #for i in range(m):
                for i in range(columns):
                    #print ("{0}, {1}, {2}".format(i,j, mode))
                    if (get_cell(array,j,i,mode)=="#") and (get_cell(array,j+direction,i,mode)!="#") and not count:
                        count = True
                        hash_count += 1
                    elif (get_cell(array,j,i,mode)=="#") and (get_cell(array,j+direction,i,mode)!="#") and count:
                        hash_count += 1
                    elif ( (get_cell(array,j,i,mode)==".") and count ) or ( (get_cell(array,j,i,mode)=="#") and (get_cell(array,j+direction,i,mode)=="#") and count ):
                        consec_list.append(hash_count)
                        hash_count = 0
                        count = False
                if count and hash_count>0:
                    consec_list.append(hash_count)
                    hash_count = 0
                    count = False
                    
                if consec_list:
                    if max(consec_list)>max_consecutive:
                        max_consecutive = max(consec_list)
        
        return max_consecutive
                    

num_of_test_cases = int(input())
n, m = [int(i) for i in input().split()]


for i in range(num_of_test_cases):
    array = []

    for j in range(n):
        row = input()
        array.append(row)
        
    print ( max ( calc_maximum_border(array,n,m,"UP"), calc_maximum_border(array,n,m,"DOWN"), calc_maximum_border(array,n,m,"LEFT"), calc_maximum_border(array,n,m,"RIGHT") ) )
