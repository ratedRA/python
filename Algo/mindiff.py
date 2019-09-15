import math
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

i = len(a)-1
j = len(b)-1
k = len(c)-1

min_diff = abs(max(a[i],b[j],c[k])-min(a[i],b[j],c[k]))
while i>-1 and j>-1 and k>-1:
	curr_min = abs(max(a[i],b[j],c[k])-min(a[i],b[j],c[k]))

	if curr_min<min_diff:
		min_diff = curr_min

	sel = max(a[i],b[j],c[k])
	if sel == a[i]:
		i-=1
	elif sel == b[j]:
		j-=1
	else:
		k-=1

print(min_diff)