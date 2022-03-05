class Solution:
    def hIndex(self, citations):
        left = 0
        right = len(citations)-1
        
        while left<=right:

            mid  = left + (right - left)//2

            if citations[mid] >= (len(citations)-mid):
                right = mid -1

            else:
                left = mid + 1

        return len(citations) - left



sol = Solution()
# print(sol.hIndex([0,1,3,5,6])==3)

# print(sol.hIndex([0,3,40,50,60])==3)

print(sol.hIndex([0,1,2,3,4,5,6,7])==4)

 
            
        