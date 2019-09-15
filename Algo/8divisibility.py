import math

n = input()
if len(n)>3:
	res = n[len(n)-1]+n[len(n)-2]+n[len(n)-3]
	res = res[::-1]
	#print(res)
	res = int(res)
	if res%8==0:
		print(1)
	else:
		print(0)
else:
	if int(n)%8==0:
		print(1)
	else:
		print(0)