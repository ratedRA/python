import math
from collections import defaultdict

a = list(map(int, input().split()))

x = int(math.sqrt(max(a)))
print(x)
        
divisor = defaultdict(lambda:0)

for i in range(1, x+1):
	for j in range(len(a)):
		if a[j]%i==0:
			divisor[j] += 1
			if (a[j]//i)>x:
			    divisor[j] +=1

res = []

for keys, values in divisor.items():
	res.append(values)
print(res)

