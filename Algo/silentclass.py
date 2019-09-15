import math
from collections import defaultdict

def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 

def ncr(n, r): 
  
    return (fact(n) / (fact(r)  
                * fact(n - r)))  

n = int(input())
a = []
for i in range(n):
	x = input()
	a.append(x)

d = defaultdict(lambda : 0)

for i in range(n):
	z = a[i][0]
	d[z]+=1

count_1, count_2 = 0, 0
j = 0

for keys, values in d.items():
	if values<2:
		continue
	s = values//2
	rest = values-s
	if j%2==0:
		if s>rest:
			if s>1:
				count_1+=ncr(s,2)
			if rest>1:
				count_2+=ncr(rest,2)
		else:
			if rest>1:
				count_1+=ncr(rest,2)
			if s>1:
				count_2+=ncr(s,2)
	else:
		if s>rest:
			if s>1:
				count_2+=ncr(s,2)
			if rest>1:
				count_1+=ncr(rest,2)
		else:
			if rest>1:
				count_2+=ncr(rest,2)
			if s>1:
				count_1+=ncr(s,2)
print(int(count_1+count_2))