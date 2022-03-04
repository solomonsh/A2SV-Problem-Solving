class Solution:
    def binarySearch(self, lst):
        left = 0
        right = len(lst)-1

        if lst[0] < 0:
            return 0

        if lst[right] >= 0:
            return len(lst)

        while left < right:

            mid = left + (right - left)//2

            if lst[mid] >= 0:
                if lst[mid+1] < 0:
                    return mid+1

                left = mid + 1

            elif lst[mid] < 0:
                if lst[mid-1] >= 0:
                    return mid

                right = mid - 1

    def countNegatives(self, grid):

        negativeCount = 0
        for lst in grid:

            negativeCount += len(lst) - self.binarySearch(lst)

        return negativeCount


sol = Solution()
print(sol.countNegatives([[3, -1, -3, -3, -3], [2, -2, -3, -
      3, -3], [1, -2, -3, -3, -3], [0, -3, -3, -3, -3]]) == 16)
# print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
# print(sol.countNegatives([[-12]]))

print(sol.countNegatives([[8, -2, -2, -2, -4, -5, -5], [-2, -3, -3, -4, -4, -5, -5], [-2, -5, -5, -5, -5, -5, -5], [-3, -5, -5, -5, -5, -5, -5],
      [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5]]))
