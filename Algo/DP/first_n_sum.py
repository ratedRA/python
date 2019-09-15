def first_n_sum(n):
	if n==1:
		return 1
	else:
		return n+first_n_sum(n-1)

n = int(input())
print(first_n_sum(n))
