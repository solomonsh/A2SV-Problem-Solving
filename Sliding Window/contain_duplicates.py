class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        dict_values = {}
        
        for i,n in enumerate(nums):
            if n not in dict_values:
                dict_values[n] = [i]
            else:
                if abs(dict_values[n][-1] - i)<=k:
                    return True
                
                dict_values[n] += [i]
                
        return False