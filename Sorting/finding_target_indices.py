
class Solution:

    # Approach one using sort method 
    # Time complexity N*log n
    # Space complexity n
    def targetIndices(self, nums, target):
        
        nums.sort()
        
        results = []
        
        for i,n in enumerate(nums):
            if n == target:
                results.append(i)
        
        return results
    
    # Approach two using counting sort
    # Time complexity n+k, where k is maximum number in the list
    # Space complexity n+k, where k is the maximum number in the list
    
    def targetIndices2(self, nums, target):
           
        counts = [0]*(max(nums)+1)

        for n in nums:
            counts[n] +=1 
        
        sorted_nums = []
        for i,n in enumerate(counts):
            if n != 0:
                sorted_nums += [i]*n

        results = []        
        for i,n in enumerate(sorted_nums):
            if n == target:
                results.append(i)
        
        return results
    

    # Approach three without sorting 
    # Time complexity n
    # Space complexity n
    def targetIndices(arr, target):
        smaller_values_count = 0

        for a in arr:
            if a < target:
                smaller_values_count+=1

        result = []
        for a in arr:
            if a == target:
                result.append(len(result)+smaller_values_count)

        return result



sol = Solution()

print(sol.targetIndices([4,5,6,8,1,2,3],5))