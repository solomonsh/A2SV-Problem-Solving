class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maximum = prices[-1]
        differnce = 0
        
        for i in range(len(prices)-2,-1,-1):
            if prices[i] > maximum:
                maximum = prices[i]
            
            else:
                differnce = max(maximum - prices[i],differnce)

        return differnce
            
        