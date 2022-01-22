class Solution:
    def maxCoins(self, piles):

        piles.sort(reverse=True)

        acc_sum = 0
        k = 0
        for i in range(0, len(piles), 2):
            pile = [piles[i], piles[i+1], piles[len(piles)-k-1]]
            acc_sum += pile[1]
            k += 1
            if k == len(piles)//3:
                break

        return acc_sum


sol = Solution()
print(sol.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
