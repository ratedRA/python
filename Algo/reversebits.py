import math

def int_to_bin_string(i):
    if i == 0:
        return ['0']*32
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    l = len(s)
    s1 = ''
    for i in range(0,32-l):
    	s1+='0'
    return s1+s

def binary_to_int(i):
	print(i)
	mul = 31
	sum1 = 0
	for j in i:
		if j=='1':
			sum1+=2**mul
		mul-=1
	return sum1


x = int(input())
res = int_to_bin_string(x)
res = res[::-1]
result = binary_to_int(res)
print(result)