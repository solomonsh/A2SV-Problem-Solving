from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
            num_counter = Counter(nums)
            
            heap = []
            result = []
         
            for n,i in num_counter.items():
               
              heapq.heappush(heap,(-1*i,n))

            for i in range(k):
                result.append(heapq.heappop(heap)[1])

            return result

sol = Solution()

print(sol.topKFrequent([3,4,2,1,5,5,7],4))