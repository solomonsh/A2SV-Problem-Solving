from cProfile import run


class Solution:

    def assignPrevious(self,val1,val2):
        previous = ""
        if  val1 < val2:
                previous = "<"
        elif val1 > val2:
                previous = ">"
        else: 
                previous = "="
            
        return previous

    def maxTurbulenceSize(self, arr):

        if len(arr) == 1 or (sum(arr)/len(arr) == arr[0]) : return 1

        left,right = 0,1
        previous = self.assignPrevious(arr[left],arr[right])

        if len(arr) == 2:
            if  previous == "=":
                return 1
            else:
                return  2

    
        oppositeSigns = {">":"<","<":">"}
        

        maxSubarrayCount = 1

        while right < len(arr)-1:

            if previous == "=":
                while arr[left] == arr[right] and right<len(arr)-1:
                    left += 1
                    right += 1
                previous = self.assignPrevious(arr[left],arr[right])

            elif  (arr[right] < arr[right+1] and previous == ">" or arr[right]>arr[right+1] and previous == "<"):
                right += 1
                previous = oppositeSigns[previous]
        
            else:
                maxSubarrayCount = max(maxSubarrayCount,right-left+1)
                left = right
                right+=1

                while arr[left] == arr[right] and right<len(arr)-1:
                    left += 1
                    right += 1

                previous = self.assignPrevious(arr[left],arr[right])

    
        maxSubarrayCount = max(maxSubarrayCount,right-left+1)
        
        return maxSubarrayCount

sol = Solution()
print(sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])==5)
            

# print(sol.maxTurbulenceSize([5,4]))
# print(sol.maxTurbulenceSize([1,1,2]))

 




        