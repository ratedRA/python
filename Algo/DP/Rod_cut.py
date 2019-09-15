def rod_cud(price, n):
	if n==0:
		return 0
	max_val = -(sys.maxsize)
	for i in range(0, n):
		max_val = max(max_val, price[i]+rod_cud(price, n-i-1))
	return max_val