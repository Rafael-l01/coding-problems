class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.prefixSum = self.calculatePrefixSum()
        self.numColunms = len(self.matrix[0])
        self.numRows = len(self.matrix)

    def calculatePrefixSum(self):
        prefixSum = [[0] * (self.numColunms + 1) for r in range(self.numRows + 1)]

        for i in range(self.numRows):
            for j in range(self.numColunms):
                prefixSum[i + 1][j + 1] = (
                    prefixSum[i + 1][j]
                    + prefixSum[i][j + 1]
                    - prefixSum[i][j]
                    + self.matrix[i][j]
                )

        return prefixSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # filling the prefixSum matrix with 0 in first row and first column shifts elements by 1
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1

        return (
            self.prefixSum[row2][col2]
            - self.prefixSum[row2][col1 - 1]
            - self.prefixSum[row1 - 1][col2]
            + self.prefixSum[row1 - 1][col1 - 1]
        )
