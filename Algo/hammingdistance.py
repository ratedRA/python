import math
from collections import defaultdict

def int_to_bin_string(i):
    if i == 0:
        return ['0']*64
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    l = len(s)
    s1 = ''
    for i in range(0,64-l):
    	s1+='0'
    return s1+s

a = list(map(int, input().split()))
count0 = [0]*64
count1 = [0]*64
mod = 10**9+7
for i in a:
	s = int_to_bin_string(i)
	#print(s)

	for j in range(len(s)):
		if s[j]=='0':
			count0[j]+=1
		else:
			count1[j]+=1
	print(count0, count1)

sum1 = 0
for i in range(0,64):
	#print(count0[i])
	sum1+=((((count1[i]%mod)*(count0[i]%mod))%mod)*2)%mod
print(sum1)

