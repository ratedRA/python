def sumSq(n):
	if n<=3:
		return n
	res = n
	for i in range(1,n):
		temp = i*i
		if temp>n:
			break
		else:
			res = min(res, 1+sumSq(n-temp))
	return res