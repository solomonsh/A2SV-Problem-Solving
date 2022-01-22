class Solution:

    def rearrangeArray(self, nums):
        nums.sort()
        median = nums[len(nums)//2]

        even_idexes = 0
        odd_indexs = 1
        result = [0]*len(nums)

        for i, n in enumerate(nums):
            if n < median:

                result[odd_indexs] = n
                if odd_indexs > len(nums):
                    odd_indexs = len(nums)-1
                odd_indexs += 2

            else:
                result[even_idexes] = n
                even_idexes += 2

        return result


sol = Solution()

print(sol.rearrangeArray([1, 2, 3, 4, 5]))
