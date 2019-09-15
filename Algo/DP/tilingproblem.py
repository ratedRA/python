def tiles(a):
	if a==1:
		return 1
	if a==2:
		return 2
	return tiles(a-1)+tiles(a-2)

a = int(input())

print(tiles(a))