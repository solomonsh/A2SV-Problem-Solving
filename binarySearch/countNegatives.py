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

    # m*log n time complexty
    def countNegatives(self, grid):

        negativeCount = 0
        for lst in grid:

            negativeCount += len(lst) - self.binarySearch(lst)

        return negativeCount


    # log m + n 
    def countNegatives1(self, grid):
        i = len(grid)-1 
        j = 0
        count = 0
        while i>=0 and j< len(grid[0]):
            print(i,j)
            print(grid[i][j])
            if grid[i][j] < 0:
                count +=len(grid[0])-j
                i -= 1
            else:
                j +=1
        return(count)


sol = Solution()

# print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
# print(sol.countNegatives([[-12]]))

# print(sol.countNegatives([[8, -2, -2, -2, -4, -5, -5], [-2, -3, -3, -4, -4, -5, -5], [-2, -5, -5, -5, -5, -5, -5], [-3, -5, -5, -5, -5, -5, -5],
#       [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5], [-5, -5, -5, -5, -5, -5, -5]]))

print(sol.countNegatives1([[6,5,-4],[4,3,-2],[3,2,1]]))
