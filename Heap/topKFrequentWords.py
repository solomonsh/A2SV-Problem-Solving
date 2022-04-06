from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        words_count = Counter(words)
        

        heap = []

        for key,val in words_count.items():
                heapq.heappush(heap,(val,key))
           
        result = []
        for i in range(len(words_count)):
            result.append(heapq.heappop(heap))
         

        result.sort(key=lambda item: (-item[0], item[1]))
        result = result[:k]
 
        return [val[1] for val in result]





sol = Solution()

print(sol.topKFrequent(["aaa","aa","a"],2))
        