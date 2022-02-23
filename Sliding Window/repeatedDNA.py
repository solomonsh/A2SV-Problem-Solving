class Solution:
    def findRepeatedDnaSequences(self, s: str):
        
        counter = {}

        subStrings = []
        result= set()

        for i in range(len(s)-9):

            sub = s[i:i+10]
            if sub in counter:
                counter[sub] += 1
                result.add(sub)

            else:
                counter[sub] = 1

        return list(result)
        
        
        
sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAAAAAAAA"))