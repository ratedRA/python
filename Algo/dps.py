import math
from collections import defaultdict

t = int(input())

while t > 0:
	s = input()
	dummy = s[::-1]
	d = defaultdict(lambda:0)
	count = 0

	if s==dummy:
		if len(s)%2==0:
			print('!DPS')
		else:
			print('DPS')
	else:
		record = []
		for i in s:
			d[i]+=1
			if d[i]%2==0:
				count +=1
				record.append(i)
		if len(s)%2==0:
			if count==((len(s)//2)-1):
				print('DPS')
			else:
				print('!DPS')

		else:
			if count>=((len(s)//2)-1):
				print('DPS')
			else:
				print('!DPS')

	t-=1

