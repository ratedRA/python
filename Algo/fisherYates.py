import random

def modified_fisher_yates(a, A, N):
	selected = [] # for storing the result.
	no_of_selections = 0
	if A<N:
		return -1
	else:
		if A==1:
			return a[0]
		for i in range(A-1, 0, -1):
			if no_of_selections>=N: # to ensure O(N) time complexity
				break
			j = random.randint(0,i-1) #Same element cannot appear twice
			selected.append(a[j])
			a[j],a[i] = a[i],a[j]
			no_of_selections+=1
			if i==1 and no_of_selections<N:
				selected.append(a[0])
				no_of_selections+=1
		return selected


a = list(map(int, input('enter the list of integers separated with space:\n').split()))
A = len(a)

N = int(input('enter the number of elements you want to select randomly from the list:'))

res = modified_fisher_yates(a, A, N)

if res==-1:
	print('ERROR: number of elements you want to select cannot exceed total number of elements in the list.')
else:
	print(res) if N>0 else print('you wanted no selection')