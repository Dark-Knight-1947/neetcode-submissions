class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):

        total = 0

        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                total += self.matrix[row][col]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)