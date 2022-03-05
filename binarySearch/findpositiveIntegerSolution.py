"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
              
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        def binarySearch(y,target):
            left = 1
            right = 1000

            while left<=right:

                mid = left + (right - left)//2

                if customfunction.f(mid,y) == target:
                    return [mid,y]

                elif customfunction.f(mid,y) > target:
                    right = mid - 1

                elif customfunction.f(mid,y) < target:
                    left = mid+1

            return -1
        
        result = []
        
        for x in range(1,1001):
                res = binarySearch(x,z)
                if res!= -1:
                    result.append(res)
        
        return result