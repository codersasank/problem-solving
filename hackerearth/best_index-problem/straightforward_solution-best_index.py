def special_sum(idx, array, length):
    cnt = idx+1
    spl_sum = 0
    for i in range(2, length-idx):
        if cnt+i>length:
            break
        for j in range(cnt, cnt+i):
            spl_sum += array[j]
            #print("J",j)
        cnt += i
    spl_sum += array[idx]
    return spl_sum

array_len = int(input())
A = list( map(int, input().split()) )
max_spl_sum = 0
for i in range(0, array_len):
    spl_sum = special_sum(i, A, array_len)
    if spl_sum > max_spl_sum:
        max_spl_sum = spl_sum
print(max_spl_sum)
