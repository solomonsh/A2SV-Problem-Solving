from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

    def balancedString(self, s: str) -> int:

        letterCounter = Counter(s)
        seenSoFar = set()

        lengthOfSub = len(s)//4

        stringToBeReplaced = ""
        for letter in s:
            if letter not in seenSoFar and letterCounter[letter] > lengthOfSub:
                seenSoFar.add(letter)
                stringToBeReplaced += ((letter) *
                                       (letterCounter[letter] - lengthOfSub))

        if stringToBeReplaced in s:
            return len(stringToBeReplaced)

        if len(stringToBeReplaced) == 0:
            return 0

        else:
            return len(self.minWindow(s, stringToBeReplaced))


sol = Solution()

print(sol.balancedString("WWEQERQWQWWRWWERQWEQ"))
