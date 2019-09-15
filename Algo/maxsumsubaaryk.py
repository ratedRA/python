from collections import deque

def maxminsumsubarray(a, k):
	sum1 = 0
	ma = deque()
	mi = deque()
	n = len(a)
	for i in range(k):

		while (len(ma)>0 and a[ma[-1]]<=a[i]):
			ma.pop()
		while (len(mi)>0 and a[mi[-1]]>=a[i]):
			mi.pop()

		ma.append(i)
		mi.append(i)

	for i in range(k, n):

		sum1 += a[ma[0]]+a[mi[0]]

		while (len(ma)>0 and ma[0]<=i-k):
			ma.popleft()
		while (len(mi)>0 and mi[0]<=i-k):
			mi.popleft()

		while (len(ma)>0 and a[ma[-1]]<=a[i]):
			ma.pop()

		while (len(mi)>0 and a[mi[-1]]>=a[i]):
			mi.pop()

		ma.append(i)
		mi.append(i)
	sum1+= a[ma[0]]+a[mi[0]]

	return sum1



a = list(map(int, input().split())
k  int(input())