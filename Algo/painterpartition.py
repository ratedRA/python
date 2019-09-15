import math

p = int(input())
board = list(map(int, input().split()))
t = int(input())

l = max(board)
h = sum(board)
presum = [0]*len(board)
presum[0] = board[0]
for i in range(1, len(board)):
	presum[i] += presum[i-1]+board[i]
ans = 0
flag = 0
print(presum)
while l<h:
	mid = (l+h)//2
	count = 1
	sum1 = 0
	for i in range(len(board)):
		sum1 += board[i]

		if sum1>mid:
			sum1 = board[i]
			count+=1

	print(mid, count)
	if count <= p:
		h = mid
	elif count > p:
		l = mid+1
	
mod = 10**7+3

print((l%mod)*(t%mod)%mod)