class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):

            if len(stack) == 0 or temp <= stack[-1][0]:
                stack.append((temp, index))

            elif temp > stack[-1][0]:

                while stack and temp > stack[-1][0]:
                    
                    poped_element = stack.pop()
                    answers[poped_element[1]] = index - poped_element[1]

                stack.append((temp, index))

        return answers


sol = Solution()

sol.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
