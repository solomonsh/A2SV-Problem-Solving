
class Solution:

    def twoSum(self, nums,target):
        
        nums_dict = {}

        for i,n in enumerate(nums):
            if target-n  in nums_dict:
                return [nums_dict[target-n],i]
            else:
                nums_dict[n] = i
  
     
       

sol  = Solution()

print(sol.twoSum([2,7,11,15],9))

