def maxMin (arr,n): 
      
    # sort all numbers 
    arr.sort() 
      
    # iterate over array and with help of  
    # horner's rule calc max_sum and min_sum 
    min_sum = 0
    max_sum = 0
    for i in range(0,n): 
          
        max_sum = 2 * max_sum + arr[n-1-i]; 
        max_sum %= MOD; 
        min_sum = 2 * min_sum + arr[i]; 
        min_sum %= MOD; 
      
    return max_sum - min_sum; 

a = list(map(int, input().split()))
n = len(a)
MOD = 10**9+7
print(maxMin)