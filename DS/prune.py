def delete_node(root, k , sum1):
	if not root:
		return None
	ls = [sum1[0]+root.val]
	rs = [lsum[0]]

	root.left = delete_node(root.left, k, ls)
	root.right = delete_node(root.right, k, rs)

	sum1[0] = max(lsum[0],rsum[0])
	if sum1[0]<k[0]:
		return None
	return root
def prune(root, k):
	if not root:
		return None
	sum1 = [0]
	return delete_node(root, k, sum1)

k = []
return prune(root, k)