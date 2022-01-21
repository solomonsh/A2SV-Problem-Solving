 
# Approach using bubble sort
# Time complexity N^2
# Space complexity N

class Solution:
    def compare(self, num1,num2):
            if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
                return True
            else:
                return False
         

    def largestNumber(self, nums):
            n = len(nums)
    
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if not self.compare(nums[j],nums[j+1]) :
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]

            if nums[0] == 0:
                return str(0)
            return "".join(str(n) for n in nums)


