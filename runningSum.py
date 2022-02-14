class Solution:
    def runningSum(self, nums):
        
        runningSum = [0]*len(nums)
        
        runningSum[0] = nums[0]
        
        for i in range(1,len(nums)):
            
            runningSum[i] = runningSum[i-1]+nums[i] 
                      
                       
        return runningSum