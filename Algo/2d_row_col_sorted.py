def find_num(m, num):
	i = 0
	n = len(m[0])
	j = n-1

	while (j>=0 and i<len(m)):
		if m[i][j]==num:
			return i*1009+j
		elif m[i][j]>num:
			j-=1
		else:
			i+=1
	return -1
