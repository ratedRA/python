#!/usr/bin/env python
import sys

def checker(s):
	openBracket = ['(','{','[']
	closeBracket = [')','}',']']
	stack = []
	for parentheses in s:
		if parentheses in openBracket:
			stack.append(parentheses)
		elif parentheses in closeBracket:
			if len(stack)>0:
				if stack[-1]==openBracket[closeBracket.index(parentheses)]:
					stack.pop()
				else:
					return 0
			else:
				return 0
	if len(stack)==0:
		return 1
try:
    s = str(sys.argv[1])
except:
    print('enter input string')
    exit()
#print(s)
res = checker(s)
if res==1:
	print('true')
else:
	print('false')