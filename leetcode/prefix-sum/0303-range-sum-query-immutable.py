class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.prefixSum = self.calculatePrefixSum()

    def calculatePrefixSum(self):
        prefixSum = [0] * 10001
        for i in range(len(self.nums)):
            prefixSum[i + 1] = prefixSum[i] + self.nums[i]

        return prefixSum

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]
