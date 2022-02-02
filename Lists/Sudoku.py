class Solution:
    def isValidSudoku(self, board):

        big = set()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    curent = board[i][j]

                    if (i, curent) in big or (curent, j) in big or (i//3, j//3, curent) in big:
                        return False

                    big.add((i, curent))
                    big.add((curent, j))
                    big.add((i//3, j//3, curent))
        return True


sol = Solution()

 