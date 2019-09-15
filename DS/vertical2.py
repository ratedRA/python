from collections import defaultdict

def vertical_traversal(root):
	m = defaultdict(list)
	m[0].append(root.val)

	hd = defaultdict()
	hd[root] = 0

	q = []
	q.append(root)
	while q:
		ele = q.pop(0)

		if ele.left:
			hd[ele.left] = hd[ele]-1
			m[hd[ele.left]].append(ele.left.val)
			queue.append(ele.left)

		if ele.right:
			hd[ele.right] = hd[ele]+1
			m[hd[ele.right]].append(ele.right.val)
			queue.append(ele.right)

	m = sorted(m.items(), key = lambda x:x[0])
	res = []
	for i in m:
		res.append(i[1])
	return res