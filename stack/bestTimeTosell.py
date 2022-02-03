class Solution:
    def maxProfit(self, prices):

        stack = []
        max_price = 0
        for price in prices:
            if len(stack) == 0:
                stack.append(price)

            if price < stack[-1]:
                stack.append(price)
            elif (price - stack[-1]) > max_price:
                max_price = (price - stack[-1])

        return max_price


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
