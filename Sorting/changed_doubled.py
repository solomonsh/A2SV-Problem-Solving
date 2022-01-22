from collections import Counter

# Approach 1 Using dictionary
# Time complexity n*log n
# Space complexity n

class Solution:
    def findOriginalArray(self, changed):

        changedCounter = Counter(changed)
        changed.sort()

        result = []
        zero_seen = False

        for c in changed:
            if changedCounter[c] == 0:
                continue
            if c == 0 and not zero_seen:
                zero_seen = True
                if changedCounter[c] % 2 == 0:
                    result += [0] * (changedCounter[c]//2)
                else:
                    return []
            if changedCounter[2*c] == 0:
                return []

            if 2*c not in changedCounter:
                return []

            if c != 0:
                result += [c]

            changedCounter[c] -= 1
            changedCounter[2*c] -= 1

        return result


sol = Solution()


print(sol.findOriginalArray([1, 3, 4, 2, 6, 8]))
