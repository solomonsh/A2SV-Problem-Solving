
# Selection sort 
# Time Complexity N^2
# Space Complexity 1

class Solution:
    def selectionSort(self, arr,n):
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[j] < arr[i]:
                    arr[j],arr[i] = arr[i],arr[j]
        return arr

sol = Solution()
print(sol.selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1],10))
