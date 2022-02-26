
class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen) -> int:

        firstSubarray = []

        maxSum = sum(nums[:firstLen])

        left = 1
        right = firstLen

        while right<len(nums):
            current_sum = sum(nums[left:right+1])
            maxSum = max(current_sum,maxSum)

            left += 1
            right += 1
        
        return maxSum


sol = Solution()
print(sol.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3))