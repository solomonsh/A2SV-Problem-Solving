class Solution:
    def pivotIndex(self, nums):

        prefixSum = [0]*len(nums)

        prefixSum[0] = nums[0]

        for i in range(1, len(nums)):

            prefixSum[i] = prefixSum[i-1]+nums[i]

        for i in range(len(prefixSum)):

            left_sum = prefixSum[i-1] if i > 0 else 0
            right_sum = prefixSum[len(prefixSum)-1]-prefixSum[i-1] - \
                nums[i] if i > 0 else prefixSum[len(prefixSum)-1]-nums[i]

            if left_sum == right_sum:
                return i

        return -1


sol = Solution()

print(sol.pivotIndex([2, 1, -1]))
