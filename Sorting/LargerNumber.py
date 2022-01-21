
# Approach using sort
# Time complexity n log n
# Space complexity N    

class LargerNumKey(str):
    def __lt__( num1, num2):
        if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
            return True
        else:
            return False

class Solution:
    
    def largestNumber(self, nums):
        nums = sorted(nums,key = LargerNumKey)

        if nums[0] == 0:
            return str(0)
        return "".join(str(n) for n in nums)


 
sol = Solution()

print(sol.largestNumber([3, 30, 34, 5, 9]))
