def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
    #print(lps)
  
    i = 0 # index for txt[] 
    while i < N and j<M: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            return i-j
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    return -1
def computeLPSArray(string,M,lps):  
  
    #lps = [None] * M  
  
    length = 0
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
  

text = input()
pat = input()
res = KMPSearch(pat, text)
print(res)