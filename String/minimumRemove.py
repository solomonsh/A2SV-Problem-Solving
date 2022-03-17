class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        listS = list(s)
        indexs = set()

        for i in range(len(s)):
            if s[i] == ")":
                if len(stack) != 0:
                    if stack[-1][0] == "(":
                        stack.pop()
                    else:
                        stack.append((")", i))

                else:
                    stack.append((")", i))

            elif s[i] == "(":
                stack.append(("(", i))

        for i in stack:
            indexs.add(i[1])

        result = []
        for i in range(len(listS)):

            if i not in indexs:
                result.append(listS[i])

        return "".join(result)


sol = Solution()
 