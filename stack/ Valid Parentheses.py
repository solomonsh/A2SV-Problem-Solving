class Solution:
    def isValid(self, st):

        parentheses = {")": "(", "]": "[", "}": "{"}
        stack = []

        for s in st:
            if s in "[({":
                stack.append(s)

            else:
                if stack:
                    if stack.pop() != parentheses[s]:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


sol = Solution()
 
