class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        words_in_window = {s[0]: 1}

        left = 0
        right = 1
        max_count = 1

        count = 1
        while right < len(s):
            if s[right] in words_in_window.keys():
                left += 1
                words_in_window = {s[left]: 1}
                right = left + 1
                count = 1

            else:
                words_in_window[s[right]] = 1
                count += 1
                right += 1

            max_count = max(max_count,count)

        return max_count


sol = Solution()
print(sol.lengthOfLongestSubstring("PWWWWKEW"))

# print(sol.lengthOfLongestSubstring("abcabcbb"))
