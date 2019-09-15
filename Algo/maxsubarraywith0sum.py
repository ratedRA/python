import math
from collections import defaultdict
a = list(map(int, input().split()))
hash_map = {} 
  
 
max_len = 0

curr_sum = 0
 
for i in range(len(a)):
      
    curr_sum += a[i] 

    if arr[i] is 0 and max_len is 0: 
        max_len = 1

    if curr_sum is 0: 
        max_len = i+1

    if curr_sum in hash_map: 
        max_len = max(max_len, i - hash_map[curr_sum] ) 
    else: 

        hash_map[curr_sum] = i 

return max_len