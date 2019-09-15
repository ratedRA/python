import math

a = list(map(int, input().split()))
b = int(input())

a.sort()
x = sum(a[:b])
y = sum(a[-b:])

print(max(abs(sum(a)-2*x),abs(sum(a)-2*y)))