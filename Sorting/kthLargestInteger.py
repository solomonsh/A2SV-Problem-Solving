
import heapq
class Solution:

    # Approach 1 using heaps, 
    # Time complexity n* log n
    # Space complexity n
    def kthLargestNumber(self, nums,k):

        heap = []
        for el in nums:  
            if len(heap)<k:
                heapq.heappush(heap, int(el))

            else:
                heapq.heappush(heap,int(el))
                heapq.heappop(heap)

        return str(heapq.heappop(heap))


 
sol = Solution()

print(sol.kthLargestNumber(["2","21","12","1"],3))