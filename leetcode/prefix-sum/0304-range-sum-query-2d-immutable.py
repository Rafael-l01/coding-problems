class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.prefixSum = self.calculatePrefixSum()

    def calculatePrefixSum(self):
        prefixSum = [
            [0] * (len(self.matrix[0]) + 1) for i in range(len(self.matrix) + 1)
        ]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                prefixSum[i + 1][j + 1] = (
                    prefixSum[i + 1][j]
                    + prefixSum[i][j + 1]
                    - prefixSum[i][j]
                    + self.matrix[i][j]
                )

        return prefixSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixSum[row2 + 1][col2 + 1]
            - self.prefixSum[row2 + 1][col1 - 1 + 1]
            - self.prefixSum[row1 - 1 + 1][col2 + 1]
            + self.prefixSum[row1 - 1 + 1][col1 - 1 + 1]
        )
