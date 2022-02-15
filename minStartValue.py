class Solution:
    def minStartValue(self, nums):

        prefixSum = [0]*len(nums)

        prefixSum[0] = nums[0]

        for i in range(1, len(nums)):

            prefixSum[i] = prefixSum[i-1] + nums[i]

        minVal = min(prefixSum)

        return 1-minVal if minVal < 0 else 1
