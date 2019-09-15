def IDsOfPackages(truckSpace, packagesSpace):
    
    # we can use two pointer approach.
    # for that we will need to sort the array
    reserveSpace = 30
    from collections import defaultdict
    
    store_id = defaultdict(lambda:int)
    for i in range(len(packagesSpace)):
        store_id[packagesSpace[i]] = i
    
    packagesSpace.sort()
    print(packagesSpace)
    l = 0
    n = len(packagesSpace)
    r = n-1
    while l<r:
        sum1 = packagesSpace[l]+packagesSpace[r]
        print(sum1,l,r)
        if truckSpace-sum1==reserveSpace:
            return [store_id[packagesSpace[l]], store_id[packagesSpace[r]]]
        
        elif truckSpace-sum1>reserveSpace:
            l+=1
        else:
            r-=1

n = int(input())
l = list(map(int, input().split()))
print(IDsOfPackages(n,l))
