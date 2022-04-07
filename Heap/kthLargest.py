import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-1*n for n in nums]
        heapq.heapify(heap)
        
        count = 0 
        while count < k-1:
            heapq.heappop(heap)
            count +=1 
        
        return -1*heapq.heappop(heap)
        