from collections import Counter
import heapq

class Solution:
    # time complexity n log n 
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

    # time complexity k log n 
    def topKFrequentOptmized(self,words,k):

        wordToFreq = Counter(words)

        maxHeap = []

        for word in wordToFreq:
            maxHeap.append([wordToFreq[word] * (-1), word])

        heapq.heapify(maxHeap)

        res = []

        while len(res) < k:
            res.append(heapq.heappop(maxHeap)[1])

        return res


sol = Solution()

 