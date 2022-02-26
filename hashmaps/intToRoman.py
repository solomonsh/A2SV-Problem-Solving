class Solution:
    def assignValues(self, n):
        n = int(n)
        mapper = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
                  90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

        result = ""

        if n in mapper:
            return mapper[n]

        elif n <= 3:
            result += mapper[1]*n
            return result
        
        elif n > 1000:
                return mapper[1000]*(n//1000)
        else:
            prev = 0
            for m in mapper.keys():
                if m > n:
                    result += mapper[prev]
                    result += self.assignValues(n-prev)
                    
                    return result
                prev = m

    def intToRoman(self, num: int) -> str:

        result = ""
        numStr = str(num)
        if num <= 10:
            return self.assignValues(num)

        
        for i in range(len(numStr)):
            val = (numStr[i]) + ("0"*(len(numStr)-1-i))
            result += self.assignValues(val)

        return result


sol = Solution()
print(sol.intToRoman(3999))
