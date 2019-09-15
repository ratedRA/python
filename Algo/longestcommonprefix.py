import math
from collections import defaultdict

a = list(input().split())
j = 0
min1 = 999999999999
for i in a:	
	if len(i)<min1:
		min1 = len(i)
		mystr = i

d = defaultdict(lambda:None)

for i in range(len(mystr)):
	d[i] = mystr[i]

j = 0
flag = 0
while j<len(mystr):
	for i in range(len(a)):
		if a[i][j] == d[j]:
			continue
		else:
			flag = 1
			break
	if flag:
		break
	else:
		j+=1

print(mystr[0:j])
