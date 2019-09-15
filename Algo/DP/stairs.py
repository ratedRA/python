def ways(n):
	if n==1:
		return 1
	if n==2:
		return 2
	return ways(n-1)+ways(n-2)

n = int(input())
countWays = ways(n)
print(countWays)