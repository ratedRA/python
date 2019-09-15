def findMinMax(root, min1, max1, hd):
	if root is None:
		return None
	if hd<min1[0]:
		min1[0] = hd
	if hd>max1[0]:
		max1[0] = hd
	findMinMax(root.left, min1, max1, hd-1)
	findMinMax(root.right, min1, max1, hd+1)

	#return min1, max1


def vertical_traversal(root, line_no, hd, res):
	if root is None:
		return None:

	if hd == line_no:
		res.append(root.val)

	vertical_traversal(root.left, line_no, hd-1, res)
	vertical_traversal(root.right, line_no, hd+1, res)

def extreme_level(root):
	min1 = [0]
	max1 = [0]
	res = []
	findMinMax(root, min1, max1, 0)
	m = []
	for line_no in (min1[0], max1[0]+1):
		res = []
		vertical_traversal(root, line_no, 0, res)
		m.append(res)
	return m
 