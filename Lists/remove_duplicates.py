class Solution:
    def removeDuplicates(self, nums):

        if len(nums)<2:
            return nums

        left_pointer = 0
        right_pointer = 1

        while right_pointer< len(nums):

            if nums[right_pointer] == nums[left_pointer]:
                right_pointer+=1
            
            else:
                nums[left_pointer+1] = nums[right_pointer]
                left_pointer += 1
        

        return left_pointer+1


sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

            
            



        