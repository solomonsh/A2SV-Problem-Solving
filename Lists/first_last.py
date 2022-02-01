from collections import Counter
class Solution:
    def searchRange(self, nums,target):
        
        def search(x):
            low = 0
            high = len(nums)     

            while low < high:
                mid = (low + high) // 2
                if nums[mid] < x:
                    low = mid+1
                else:
                    high = mid    

            return low
        
        low = search(target)
        high = search(target+1)-1
        
        if low <= high:
            return [low, high]
                
        return [-1, -1]
        

sol = Solution()

print(sol.searchRange([8,8,8,8,8],7))

# print(sol.searchRange([1],0))