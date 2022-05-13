class Solution:
    def countOrders(self, n: int) -> int:
        
        memo = [1]
        
        for i in range(2,n+1):
            prev_gaps = (((i-1)*2+1)*memo[-1]*i)%(10**9 + 7)
            memo.append(prev_gaps)
            
        return memo[-1]
                
            
            