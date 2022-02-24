class Solution:
    def majorityElement(self, nums):
        
        size = len(nums)//3
        
        nums_counter = {}
        result  = set()
        
        for n in nums:
            nums_counter[n] = 1 + nums_counter.get(n,0)
            
            if nums_counter[n] > size:
                result.add(n)
                    
        return list(result)