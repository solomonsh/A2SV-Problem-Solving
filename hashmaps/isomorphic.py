class Solution:
    def isIsomorphic(self, s, t):

        expected = ""
        
        mapper  = {}
        seen  = set()

        for i in range(len(s)):
            char = ""
            if s[i] not in mapper:
                if t[i] in seen:
                    return False

                char =  t[i]
                mapper[s[i]] = char
                seen.add(t[i])
                
            else: 
                char = mapper[s[i]]
            expected += char
     
    
        return expected == t

sol = Solution()
print(sol.isIsomorphic("badc","baba"))
 
 