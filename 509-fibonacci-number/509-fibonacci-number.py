class Solution:
 
    def fib(self, n: int) -> int:
        
        memo = {}
        def dp(n):
            if n == 0 or n == 1:
                return n
            
            if n in memo:
                return memo[n]
            else:
                res = dp(n-1)+dp(n-2)
                memo[n] = res
                return res
                
        return dp(n)