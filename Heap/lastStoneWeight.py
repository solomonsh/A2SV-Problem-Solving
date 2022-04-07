import heapq

class Solution:
    def lastStoneWeight(self, stones):
        heap = [-1*stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap)>1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            
            smash_result = abs(stone1-stone2)
            
            if smash_result>0:
                heapq.heappush(heap,-1*smash_result)
                
        return -1*heap[0] if len(heap)>0 else 0



sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))