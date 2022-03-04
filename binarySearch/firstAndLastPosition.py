class Solution:
    def searchRange(self, nums, target):
        def binarySearch(nums, target):
            left = 0
            right = len(nums)-1

            while left <= right:

                mid = left + (right - left)//2

                if nums[mid] == target:
                    if nums[mid-1] != target or mid == 0:
                        return (mid, left)
                    right = mid - 1

                if nums[mid] > target:
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

            return (-1, left)

        low = binarySearch(nums, target)[0]
        high = (binarySearch(nums, target+1))
        high = high[0]-1 if high[0] != -1 else high[1]-1

        if low == -1:
            return [-1, -1]

        return [low, high]


sol = Solution()

print(sol.searchRange([8, 8, 8, 8, 8, 8], 8))
print(sol.searchRange([1, 2, 3], 1))
