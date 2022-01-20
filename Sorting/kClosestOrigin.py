import math


class Solution:
    def kClosest(self, points, k):
        distances = {}
        for point in points:
            point = tuple(point)
            distance = math.sqrt((point[0]-0)**2 + (point[1]-0)**2)

            if point in distances:
                distances[point] = [distance, distances[point][1]+1]
            else:
                distances[point] = [distance, 1]

        results = []
        sorted_distance = {k: v for k, v in sorted(
            distances.items(), key=lambda item: item[1][0])}

        for s in sorted_distance.items():
            x = list(s[0])
            s1 = list(s[1])[1]
            if s1 != 0:
                results += [x]*s1
            else:
                results += [x]

        return results[:k]


sol = Solution()
points = [[2, 2], [2, 2], [3, 3], [2, -2], [1, 1]]


print(sol.kClosest(points, 2))
