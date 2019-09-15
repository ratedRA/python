class Solution:
	# @param A : string
	# @return an integer
	def solve(self, s):
	    res1,res2 = 0,0
        n = len(s)
        count10 = [0]*n
        count10[0] = 1-int(s[0])
        for i in range(1,len(s)):
        	count10[i] = count10[i-1]
        	if s[i]=='0':
        		count10[i]+=1
        for i in range(len(s)):
        	if s[i]=='1':
        		res1+=count10[i]
        
        count01 = [0]*n
        count01[n-1] = 1-int(s[n-1])
        for i in range(n-2,-1,-1):
        	count01[i] = count01[i+1]
        	if s[i]=='0':
        		count01[i]+=1
        for i in range(len(s)):
        	if s[i]=='1':
        		res2+=count01[i]
        return(min(res1,res2))
