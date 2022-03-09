class Solution:

    def search_range(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] > nums[mid+1]:
                left = mid+1
                break
            elif nums[mid] < nums[-1]:
                right = mid-1

            elif nums[mid] > nums[-1]:
                left = mid + 1

        if left == 0 and nums[left] > nums[left+1]:
            left = left + 1

        return [0, left-1] if target > nums[-1] else [left, len(nums)-1]

    def search(self, nums, target):

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        start = self.search_range(nums, target)[0]
        end = self.search_range(nums, target)[1]

        while start <= end:

            mid = start + (end - start)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid - 1

        return -1


sol = Solution()
print(sol.search([5], 5))
