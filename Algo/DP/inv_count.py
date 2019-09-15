def merge_sort(a):
	inv_count = 0
	if len(a)>1:
		n = len(a)
		mid = n//2
		first = a[0:mid]
		second = a[mid:n]
		
		inv_count += merge_sort(first)
		inv_count += merge_sort(second)
		inv_count += merge(first, second, a)
	return inv_count
def merge(first, second, a):
	l1 = len(first)
	l2 = len(second)
	# print(first,second)
	# print(a)
	count = 0
	i = 0
	j = 0
	k = 0
	while(i<l1 and j<l2):
		if first[i]<second[j]:
			a[k] = first[i]
			i+=1
		else:
			a[k] = second[j]
			count+=(l1-i)
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
	return count

a = list(map(int, input().split()))
res = merge_sort(a)
print(res)
