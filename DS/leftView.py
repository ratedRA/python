def leftView(root,m):
	if root.left:
		m.append(root.left.val)
		leftView(root.left, m)