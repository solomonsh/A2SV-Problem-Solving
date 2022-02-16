class Solution:
    def minSubArrayLen(self, target, nums):
        nums.append(0)
        left = 0
        right = 0

        cur_sum =  0
        min_length = len(nums)
        found = False
        
        while right < len(nums) and left<=right:

            if cur_sum >= target:   
                found = True
                min_length = min(min_length, right-left)
                cur_sum -= nums[left]
                left += 1

            else:
                cur_sum += nums[right]
                right += 1

        return min_length if found else 0


sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))


 
