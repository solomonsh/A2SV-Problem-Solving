class Solution:

    def combineChars(self, chars1, chars2):
        result = []
        for c1 in chars1:
            for c2 in chars2:
                result.append(c1+c2)

        return result

    def letterCombinations(self, digits):
        mapping = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                   '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        if len(digits) == 0:
            return []

        result = list(mapping[digits[0]])

        for i in range(1, len(digits)):

            result = self.combineChars(result, mapping[digits[i]])

        return result


sol = Solution()
print(sol.letterCombinations("23"))
