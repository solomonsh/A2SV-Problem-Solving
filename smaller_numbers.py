class Solution:

    # Time complexity n*log n
    # Space complexity n
    def smallerNumbersThanCurrent(self, nums):
        nums_sorted = nums.copy()
        nums_sorted.sort()

        nums_dict = {}

        for i, v in enumerate(nums_sorted):
            if v not in nums_dict:
                nums_dict[v] = i

        result = []

        for n in nums:
            result.append(nums_dict[n])

        return result


sol = Solution()
print(sol.smallerNumbersThanCurrent([7, 7, 7, 7]))
