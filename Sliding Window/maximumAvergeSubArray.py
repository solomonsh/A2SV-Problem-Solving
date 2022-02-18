class Solution:
    def findMaxAverage(self, nums, k):

        left = 0
        right = k

        cur_sum = sum(nums[0:k])
        max_average = cur_sum/k

        while right < len(nums):
            cur_sum -= nums[left]
            cur_sum += nums[right]

            cur_average = cur_sum / k

            max_average = max(max_average, cur_average)

            left += 1
            right += 1

        return max_average


sol = Solution()

print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))

print(sol.findMaxAverage([5], 1))
