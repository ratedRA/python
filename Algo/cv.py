import math

t = int(input())

while t>0:
	n = int(input())
	s = input()
	vowels = ['a','e','i','o','u']
	count= 0
	for i in range(0, n-1):
		if s[i] not in vowels:
			if s[i+1] in vowels:
				count+=1
	print(count)
	t-=1