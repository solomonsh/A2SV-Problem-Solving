class Solution:
    def numberOfWeakCharacters(self, properties):

        properties = sorted(properties, key=lambda x: (x[0], -x[1]))

        stack = []

        count = 0

        for prop in properties:

            if len(stack) == 0:
                stack.append(prop)

            else:
                while len(stack) > 0 and prop[1] > stack[-1][-1] and prop[0] > stack[-1][0]:
                    count += 1
                    stack.pop()

                stack.append(prop)

        return count


sol = Solution()

sol.numberOfWeakCharacters([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]])
