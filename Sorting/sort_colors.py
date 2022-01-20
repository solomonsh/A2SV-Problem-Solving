class Solution:
    def sortColors(self, nums):

        for i in range(1, len(nums)):

            if nums[i] < nums[i-1]:

                for j in (i, -1, -1):
                    if nums[j-1] <= nums[j]:
                        break
                    else:
                        nums[j], nums[j-1] = nums[j-1], nums[j]


    def sortColors2(self, nums):

        counts = [0] * 3
        for n in nums:
            counts[n] += 1

        position = 0
        for i, n in enumerate(counts):
            for j in range(position, position+n):
                nums[j] = i
                position += 1

        return nums


sol = Solution()

print(sol.sortColors2([0, 2, 1, 1]))
