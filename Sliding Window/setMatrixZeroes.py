from cmath import inf


class Solution:

    def setRowToZeroes(self, matrix, row):
        for i in range(len(matrix[row])):
            if matrix[row][i] != 0:
                matrix[row][i] = inf

    def setColumnToZeroes(self, matrix, column):
        for j in range(len(matrix)):
            if matrix[j][column] != 0:
                matrix[j][column] = inf

    def setZeroes(self, matrix):

        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[i][k] == 0:
                    self.setRowToZeroes(matrix, i)
                    self.setColumnToZeroes(matrix, k)
                    
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[i][k] == inf:
                    matrix[i][k] = 0

        return matrix


sol = Solution()
sol.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
