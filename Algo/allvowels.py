from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
if isPrime(n):
	print(-1)
else:
	#print('no')
	x = n//5
	if x<5:
		print(-1)
	else:
		j = 5
		while 1:
			if n%j==0:
				break
			else:
				j+=1
		a = j
		b = n//j
		if b<5:
			print(-1)
		else:
			#print(a,b)
			first = 'aeiou'
			second = 'eioua'
			third = 'iouae'
			fourth = 'ouaei'
			fifth = 'uaeio'
			extra = b-5
			sextra = ''
			res =''
			for i in range(extra):
				sextra+='b'
			for i in range(a+1):
				if i%6==0:
					res += first
					for _ in range(extra):
						res+='a'
				elif i%6==1:
					res += second
					for _ in range(extra):
						res+='e'
				elif i%6==2:
					res += third 
					for _ in range(extra):
						res+='i'
				elif i%6==3:
					res += fourth 
					for _ in range(extra):
						res+='o'
				elif i%6==4:
					res += fifth 
					for _ in range(extra):
						res+='u'

			print(res)