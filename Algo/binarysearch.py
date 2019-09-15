a = list(map(int, input().split()))
l = 0
h = n-1
target = int(input())

while l<=h:
	mid = (l+h)//2

	if a[mid] == target:
		print(mid)
		break
	elif a[mid]>target:
		h = mid-1
	else:
		l = mid+1