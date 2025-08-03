import heapq

def find_mean_median_mode(arr, k):
    heap_arr = [-num for num in arr]
    heapq.heapify(heap_arr)
    cnt = 0
    sum_k = 0
    freq = dict()
    k_arr = list()
    while (cnt < k):
        num = -heapq.heappop(heap_arr)
        sum_k += num
        cnt += 1
        k_arr.append(num)
        freq[num] = freq.get(num, 0) + 1
    mean = sum_k / k
    median = k_arr[k//2] if k%2==1 else (k_arr[(k//2)-1] + k_arr[k//2])/2
    mode = max(freq, key=freq.get)
    print ( k_arr )
    return (mean, median, mode)


arr = [1.3, 2.3, 2.3, 4.3, 4.3, 3.3, 6.3]
print ( find_mean_median_mode(arr, 3) )
        
    
