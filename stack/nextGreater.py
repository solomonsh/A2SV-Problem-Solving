
class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        result = []
        result1 = [-1]*len(nums1)

        for num in enumerate(nums2):

            if len(stack) == 0 or num < stack[-1]:
                stack.append(num)

            elif num > stack[-1]:
                result.append((num, stack.pop()))
                if len(stack) != 0: 
                    while len(stack) > 0 and stack[-1] < num:
                        result.append((num, stack.pop()))
                stack.append(num)

        while stack:
            result.append((-1, stack.pop()))

        for num in result:
            if num[1] in nums1:
                result1[nums1.index(num[1])] = num[0]

        return result


sol = Solution()

sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
