def knapsack_recursive(w, wt, val, n):
	if n==0 or w==0:
		return 0
	if (wt[n-1]>w):
		#print(w)
		return knapsack(w, wt, val, n-1)

	return max(val[n-1]+ knapsack(w-wt[n-1], wt, val, n-1),knapsack(w, wt, val, n-1))

def knapsack_dp(w, wt, val,n):
	dp = [[0 for x in range(n)]for i in range(n)]
	for i in range(n+1):
		for j in range(n+1):
			if i==0 or j==0:
				dp[i][j] = 0
			elif wt[i-1]<=j:
				dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])
			else:
				dp[i][j] = dp[i-1][j]
	return dp[n][n]

val = [60, 100, 120] 
wt = [30, 20, 60] 
w = 50
n = len(val) 
print(knapsack(w , wt , val , n)) 