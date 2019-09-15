def merge_sort(a):
	if len(a)>1:
		n = len(a)
		mid = n//2
		first = a[0:mid]
		second = a[mid:n]
		merge_sort(first)
		merge_sort(second)
		merge(first, second, a)
def merge(first, second, a):
	l1 = len(first)
	l2 = len(second)
	# print(first,second)
	# print(a)
	i = 0
	j = 0
	k = 0
	while(i<l1 and j<l2):
		if first[i]<second[j]:
			a[k] = first[i]
			i+=1
		else:
			a[k] = second[j]
			j+=1
		k+=1
	while i<l1:
		a[k] = first[i]
		i+=1
		k+=1

	while j<l2:
		a[k] = second[j]
		j+=1
		k+=1

a = list(map(int, input().split()))
merge_sort(a)
print(a)
