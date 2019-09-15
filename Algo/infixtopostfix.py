import math

def get_precedence(a,b):
	if a=='*' or 

def in_to_postfix(s):
	stack = []
	postfix = ''
	for i in s:
		if i.isdigit():
			postfix+=i


exp = input()
in_to_postfix(exp)