class Solution:
    def calculatePrefixSumArray(self, nums):
        prefixSum = [0] * 10001
        for i, num in enumerate(nums):
            prefixSum[i + 1] = prefixSum[i] + num

        return prefixSum

    def pivotIndex(self, nums) -> int:
        prefixSum = self.calculatePrefixSumArray(nums)

        for i in range(len(nums)):
            prefixBefore = prefixSum[i]
            prefixAfter = prefixSum[len(nums)] - prefixSum[i + 1]

            if prefixBefore == prefixAfter:
                return i

        return -1
