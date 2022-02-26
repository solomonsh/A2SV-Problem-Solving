def getMinimumCost(parcels,k):

    parcelsSet = set(parcels)

    totalCost = 0

    count = 0
    i = 1

    while count != k-len(parcels):
        if i  not in parcelsSet:
            totalCost+= i
            count += 1
        i+=1
    
    return totalCost


# print(getMinimumCost([2,3,6,10,11],9))

# print(getMinimumCost([4,5,7,1],4))

# print(getMinimumCost([6,5,4,1,3],2))


print(getMinimumCost([1],1000000))