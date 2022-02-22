from collections import deque

class Solution:

    def totalFruit(self, fruits):

        if len(fruits) == 1:
            return 1

        left = 0
        right = 1

        fruitTypes = deque([fruits[left]])

        fruitsTobePicked = 2

        while right < len(fruits):

            if len(fruitTypes) == 1 and fruits[0] != fruits[right]:
                fruitTypes.append(fruits[right])

            if fruits[right] not in fruitTypes:

                fruitTypes = [fruits[right-1], fruits[right]]

                fruitsTobePicked = max(fruitsTobePicked, right-left)

                leftPrevIndex = left
                left = right-1

                while left > leftPrevIndex:
                    if fruits[left-1] == fruits[left]:
                        left -= 1
                    else:
                        break

            right += 1

        fruitsTobePicked = max(fruitsTobePicked, right-left)
        return fruitsTobePicked


sol = Solution()
