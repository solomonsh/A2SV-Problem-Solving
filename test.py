def calculateSum(num,l,r):

    prefix = [0]*len(num)

    prefix[0] = num[0]

    for i in range(1,len(num)):
        prefix[i] = prefix[i-1]+num[i]

    print(prefix)
    return prefix[r]-prefix[l-1] if l>0 else prefix[r] - prefix[l]



num = [1,2,3,4,5,6]

print(calculateSum(num,1,2))
# print(sum(num))
