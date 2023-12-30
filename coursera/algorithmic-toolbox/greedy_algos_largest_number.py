from functools import cmp_to_key

def compare(str1, str2):
    inverted = False
    if str1==str2:
        return 0
    n1 = len(str1)
    n2 = len(str2)
    if n1>n2:
        n1, n2 = n2, n1
        str1, str2 = str2, str1
        inverted = True
    for i in range(n1):
        if str1[i]!=str2[i]:
            if inverted:
                return ord(str2[i])-ord(str1[i])
            else:
                return ord(str1[i])-ord(str2[i])
    if inverted:
        return compare(str2[n1:], str1)
    else:
        return compare(str1,str2[n1:])
        
def largest_number(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=cmp_to_key(compare))
    largest = int(''.join(numbers))
    return largest

if __name__ == '__main__':
    #print ( compare ( '21' ,'2' ) )
    #print ( compare ( '812' ,'8129' ) )
    t = int(input())
    input_nums = input().split()
    print(largest_number(input_nums))
