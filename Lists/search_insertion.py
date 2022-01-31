class Solution:
    def searchInsert(self, nums, target):

        left = 0
        right = len(nums)-1


        while left<=right:

            middle = (left+right)//2

            if target == nums[middle]:
                return middle

            elif target> nums[middle]:
                left = middle+1
            
            else:
                right = middle -1
        
        return left

sol = Solution()

print(sol.searchInsert([1,3,5,6],9))


        