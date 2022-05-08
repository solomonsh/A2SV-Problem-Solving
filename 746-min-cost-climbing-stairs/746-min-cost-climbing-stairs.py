class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      
        memo = {}
        
        def dp(start):
          
            if start < 0:
                return 0
            if start == 0 or start == 1:
                return cost[start]
            
            res = 0
            if start in memo:
                return memo[start]
            else:  
                path1 = dp(start-1)
                path2 = dp(start-2)
                
                res = cost[start] + min(path1,path2)
                memo[start] = res
            
            return res
        
        return min(dp(len(cost)-1),dp(len(cost)-2))
        
      