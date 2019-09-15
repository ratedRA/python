def check(A, num,B):
    cows=1
    pos = A[0]
    for i in range(1, len(A)):
        if A[i]-pos>=num:
            cows+=1
            pos = A[i]
            if cows==B:
                return 1
    
    return 0

A = list(map(int, input().split()))
B = int(input())
l = 0
r = max(A)
A.sort()
ans = 0
while l<=r:
    mid = (l+r)//2

    if check(A, mid,B)==1:
        l = mid+1
        if mid>ans:
            ans = mid
    else:
        #print('yes')
        r = mid-1
    
print(ans)