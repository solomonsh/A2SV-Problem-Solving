class Solution:
    def minStartValue(self, nums):

        min_value = 0
        preSum = 0

        for num in nums:
            preSum += num
            min_value = min(min_value, preSum)

        return 1 - min_value
