import math
def is_prime(num):
    if num==1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
def primepartition(m):
    primes_list = dict()
    for i in range(2,m-1):
        if is_prime(i):
            primes_list[i] = True
    for prime in primes_list:
        if m-prime in primes_list:
            return True
    return False
            
    
