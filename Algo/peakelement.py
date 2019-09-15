import math
a = list(map(int, input().split()))

l = 0
h = len(a)-1
n = len(a)

while l<=h:
	mid = (l+h)//2

	if mid == n-1:
		if a[mid]>=a[mid-1]:
			print(a[mid])
			break
		else:
			h = mid-1
	elif mid == 0:
		if a[mid]>=a[mid+1]:
			print(a[mid])
			break
		else:
			l = mid+1
	elif a[mid-1]<=a[mid] and a[mid]>=a[mid+1]:
		print(a[mid])
		break
	elif a[mid-1]>a[mid]:
		h = mid-1
	else:
		l = mid+1

