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

    # Optimized solution
    # Time complexity  n
    # Space complexity n

    def smallerNumbersThanCurrent(self, nums):
        counts = [0] * 101
        result = []

        for i in range(len(nums)):
            counts[nums[i]] += 1

        previous = 0

        for i in range(len(counts)):
            if counts[i] != 0:
                temp = counts[i]
                counts[i] = previous
                previous += temp

        for n in nums:
            result.append(counts[n])

        return result


sol = Solution()
print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
