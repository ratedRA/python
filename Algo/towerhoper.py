import math
import copy

def next_step(current, towers):
	a = current
	current = current+towers[current]
	if current < len(towers):
		while towers[current] == 0:
			current -= 1
			if towers[current] != 0:
				return current
			if current == a:
				current = a+towers[a]
				break
	return current

def is_hoppable(current, towers):
	while True:
		if current >= len(towers):
			return True
		if towers[current] == 0:
			return False

		current = next_step(current, towers)

# def reverse_itr(towers):
# 	minDist = [0]*len(towers)
# 	l = len(towers)
# 	for i in range(towers):
# 		minDist[i] = l-i
# 	return minDist

towers = list(map(int, input().split()))
#minDist = reverse_itr(towers)
res = is_hoppable(0, towers)
print(res)