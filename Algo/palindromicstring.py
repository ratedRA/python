import math

def computeLPSArray(string):  
  
    M = len(string)  
    lps = [None] * M  
  
    length = 0
    lps[0] = 0  
    i = 1
    while i < M:  
      
        if string[i] == string[length]:  
          
            length += 1
            lps[i] = length  
            i += 1
          
        else:  
            if length != 0: 
              
                length = lps[length - 1]  
  
 
            else: # if (len == 0)  
              
                lps[i] = 0
                i += 1
  
    return lps


s = input()
count = 0
n = len(a)-1

news = s+'$'+s[::-1]
res = computeLPSArray(news)
print(len(s)-res[len(res)-1])