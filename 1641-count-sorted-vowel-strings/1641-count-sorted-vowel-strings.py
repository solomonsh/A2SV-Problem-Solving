class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        res = [1 for _ in range(5)]

        for i in range(n-1):
            for j in range(len(res)-2,-1,-1):
                res[j] += res[j+1]
        
        return sum(res)