import math

def all_subsets(given_array):
	subset = [None]*len(given_array)
	helper(given_array, subset, 0)

def helper(given_array, subset, i):
	if i == len(given_array):
		print(subset)
	else:
		#print(i)
		subset[i] = 'null'
		helper(given_array, subset, i+1)

		subset[i] = given_array[i]
		helper(given_array, subset, i+1)

a = list(map(int, input().split()))
all_subsets(a)
