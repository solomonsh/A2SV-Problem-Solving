class Solution:
    
    def threeSum(self, nums):
        
        res = []

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            left =  i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a+nums[left]+nums[right]

                if threeSum > 0:
                    right -= 1

                elif threeSum < 0:
                    left+=1
                else:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left += 1

        return res


# nums = [-1,0,1,2,-1,-4]
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
sol = Solution()

print(sol.threeSum(nums))
