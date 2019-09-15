def sos(n):
	dp = [1]*(n+1)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	dp[3] = 3

	for i in range(4, n):
		dp[i] = i
		for j in range(1,i+1):
			temp = j*j
			if temp>i:
				break
			else:
				dp[i] = min(dp[i], dp[i-temp])
	return dp[n]