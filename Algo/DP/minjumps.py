import sys
def min_jumps_rec(a, l, h):
	if l==h:
		return 0
	if a[l]==0:
		return -1
	jumps = -1
	min1 = sys.maxsize
	for i in range(l+1,h+1):
		if(i<=a[l]+l):
			jumps = min_jumps(a,i,h)
		if (jumps!=-1 and jumps+1<min1):
			min1 = jumps+1
	return min1

def min_jumps_dp(a):
	dp = [0]*(len(a))
	for i in range(1, len(a)):
		jumps[i] = sys.maxsize
		for j in range(0,i):
			if (a[j]+j>=i):
				jumps[i] = min(jumps[i], jumps[j]+1)
				break
	return jumps[n-1]

a = list(map(int, input().split()))
print(min_jumps(a, 0, n-1))