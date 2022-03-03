from collections import Counter

class Solution:

    # time complexity N
    # space complexity N
    def firstMissingPositive1(self, nums) -> int:
        nums_counter = Counter(nums)
        
        n = 1
        while n<=len(nums)+1:
            if n not in nums_counter:
                return n
            
            else:
                n+=1
                
        return 1


    # optimized for space
    # time complexity N
    # space complexity 1
    [3,0,2,1,6]
    
    def firstMissingPositive2(self, nums) -> int:
        nums = [n if n>=0 else 0 for n in nums]

        for n in nums:
            n = abs(n)
            if n-1<len(nums) and n-1>=0:
                if nums[n-1] > 0:
                     nums[n-1] = -1*nums[n-1]

                elif nums[n-1] == 0:
                    nums[n-1] = -1*(len(nums)+1)

    

        count = 1
        while count<=len(nums):

            if nums[count-1] >= 0:
                return count
            else:
                count+=1
                
        return len(nums)+1


sol = Solution()

# print(sol.firstMissingPositive2([4,1,2,-3,6,8]))
print(sol.firstMissingPositive2([1,2,0]))