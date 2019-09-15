import math

a = list(map(int,input('enter the list: ').split()))
lis = [1]*(len(a))
for i in range(1, len(a)):
	for j in range(0, i):
		if a[i] > a[j] and lis[i]<lis[j]+1:
			lis[i] = lis[j]+1

lbs = [1]*len(a)
n = len(a)
for i in range(n-2, -1, -1):
	for j in range(i, n):
		if a[i] < a[j] and lbs[i]<lbs[j]+1:
			lbs[i] = lbs[j]+1

maximum = lis[0] + lbs[0] - 1
for i in range(1 , n): 
    maximum = max((lis[i] + lbs[i]-1), maximum) 
  
return maximum 
  


print(max(lis))