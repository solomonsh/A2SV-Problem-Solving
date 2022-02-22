from collections import Counter


class Solution:
    def numberOfSubarrays(self, nums, k):

        nums = [0 if n % 2 == 0 else 1 for n in nums]

        prefixSum = [0]*len(nums)

        prefixSum[0] = nums[0]

        for i in range(1, len(nums)):

            prefixSum[i] = prefixSum[i-1]+nums[i]

        counter = Counter(prefixSum)

        result = 0

        for n in counter.keys():
            if n == k:
                result += counter[n]

            if n-k in counter:
                result += counter[n-k]*counter[n]

        return result


sol = Solution()
# print(sol.numberOfSubarrays([1,2,1,2,2,1,1,2],3))
print(sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
