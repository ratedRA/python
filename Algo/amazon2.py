def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    forwardRouteList = sorted(forwardRouteList, key=lambda x:x[1])
    returnRouteList = sorted(returnRouteList, key=lambda x:x[1])
    
    res = []
    l = 0
    n1 = len(forwardRouteList)
    n2 = len(returnRouteList)
    r = n2-1
    max1 = -99999999999
    
    while (l<n1 and r>-1):
        sum1 = forwardRouteList[l][1] + returnRouteList[r][1]
        
        if sum1<=maxTravelDist:
            if sum1>=max1:
                res.append([forwardRouteList[l][0], returnRouteList[r][0], sum1])
                max1 = sum1
            l+=1
        else:
            r-=1
    lis = []
    res = sorted(res, key = lambda x:x[2], reverse = True)
    lis.append([res[0][0],res[0][1]])
    for i in range(1, len(res)):
        if res[i][2]==res[0][2]:
            lis.append([res[i][0],res[i][1]])
        else:
            break

    return lis

n = int(input())
forwardRouteList = [[1,8],[2,7],[3,14]]
returnRouteList = [[1,5],[2,10],[3,14]]
print(optimalUtilization(n,forwardRouteList,returnRouteList))