class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dfs(index,action):
            if (index,action) in memo:
                return memo[(index,action)]
            if index >= len(nums):
                return 0
            
            maxSum = 0
            if action == "Rob":
                maxSum = nums[index] + dfs(index+1,"Jump")
                
            elif action == "Jump":
                 maxSum = max(dfs(index+1,"Rob"),dfs(index+1,"Jump"))
            
            memo[(index,action)] =  maxSum
            return maxSum 
        
        return max(dfs(0,"Jump"),dfs(0,"Rob"))