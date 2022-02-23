class Solution:
    def characterReplacement(self, s, k):

        if len(s) == 1:
            return 1

        left = 0
        right = 1

        maxReplaceLength = 1

        charInWindow = {s[left]: 1}

        while right < len(s):
            if s[right] in charInWindow:
                charInWindow[s[right]] += 1
            else:
                charInWindow[s[right]] = 1

            if (len(charInWindow.keys()) > k+1) or (sum(charInWindow.values()) - max(charInWindow.values()) > k):

                charInWindow[s[left]] -= 1
                if charInWindow[s[left]] == 0:
                    del charInWindow[s[left]]

                left += 1

            maxReplaceLength = max(maxReplaceLength, right-left+1)
            right += 1

        return maxReplaceLength


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
# print(sol.characterReplacement("ABAB",2))
# print(sol.characterReplacement("AABABBABABB",2))
