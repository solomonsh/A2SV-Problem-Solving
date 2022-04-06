from collections import Counter
import heapq

class Solution:
    # time complexity n log n
    # space complexity n+k
    def topKFrequent(self, nums, k):
            num_counter = Counter(nums)
            
            heap = []
            result = []
         
            for n,i in num_counter.items():
               
              heapq.heappush(heap,(-1*i,n))

            for i in range(k):
                result.append(heapq.heappop(heap)[1])

            return result


    # time complexity n 
    # space complexity n+k
    def topKFrequentBucketSort(self, nums, k):
        num_counter = Counter(nums)
        counting_sort = [[] for i in range(len(nums)+1)]
        
        for i,n in num_counter.items():
            counting_sort[n].append(i)

        result = []
        
        for i in range(len(counting_sort)-1,0,-1): 
              for n in counting_sort[i]:
                    result.append(n)
                    if len(result) == k:
                      return result


            
        return result 



sol = Solution()

print(sol.topKFrequentBucketSort([3,4,2,1,5,5,7],4))