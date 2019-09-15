def all_el(a, index):
	print(index)
	# if index<len(a):
	# 	#print(a[index])
	# else:
	# 	return 0
	for i in range(index, len(a)):
		all_el(a, i+1)
a = list(map(int, input().split()))
all_el(a,0)