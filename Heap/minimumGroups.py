import heapq

def minimumGroups(awards,k):

    heap = [award for award in awards]
    heapq.heapify(heap)

    count = 0
    temp = []
    while heap:
       
        if len(temp) == 0:
            temp.append(heapq.heappop(heap))
            if len(heap) == 0: count +=1
        
        else:
            if abs(temp[0] - heap[0])<=k:
                heapq.heappop(heap)
                if len(heap) == 0: count +=1

            else:
                count += 1
                temp = []

    return count



print(minimumGroups([1,5,4,6,8,9,2],3))
print(minimumGroups([1,13,6,8,9,3,5],4))



