from collections import Counter

class Solution:

    def findLongestSubString(self, s):

        if len(s) == 0:
            return ""

        counter = Counter(s)

        for i, letter in enumerate(s):
            if (letter.isupper() and letter.lower() not in counter) or (letter.islower() and letter.upper() not in counter):

                left = self.findLongestSubString(s[:i])
                right = self.findLongestSubString(s[i + 1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s


sol = Solution()
print(sol.findLongestSubString("YazAZbyYcAacCG"))

# print(sol.longestNiceSubstring("YazaAay"))
# print(sol.findLongestSubString("Bb"))
