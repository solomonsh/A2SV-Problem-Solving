class Solution:
    def shipWithinDays(self, weights, days):

        def canShip(days,capacity):
            cur_sum = 0
            count = 0
            for i in range(len(weights)):
                
                if cur_sum+weights[i]<=capacity:
                    cur_sum+=weights[i]
                
                else:
                    count += 1
                    cur_sum = weights[i]

            if cur_sum<=capacity:
                count+=1
           
            return False if count > days else True
            

        left = max(weights)
        right = sum(weights)

        while left<right:
            mid = left + (right - left)//2
 
            if canShip(days,mid):
                right = mid
            
            else:
                left = mid+1

      
        return right

sol = Solution()
 
