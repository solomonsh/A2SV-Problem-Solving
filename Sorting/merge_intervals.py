
class Solution:

    # Apporach 1 sorting
    # Time complexity n log n
    # Space complexity n

    def merge(self, intervals):
        intervals.sort()

        result = [intervals[0]]
        for interval in intervals:

            if result[-1][1] == interval[1]:
                continue

            if result[-1][1] >= interval[0]:
                result[-1][1] = max(interval[1], result[-1][1])

            else:
                result.append(interval)

        return result


sol = Solution()

print(sol.merge([[20, 25], [1, 4], [2, 4], [21, 24]]))
