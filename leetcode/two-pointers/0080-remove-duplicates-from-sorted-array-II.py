from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        actualNumber = nums[0]
        nextPosition = 1
        appearances = 1

        for i in range(1, len(nums)):
            if nums[i] == actualNumber and appearances < 2:
                nums[nextPosition] = nums[i]
                nextPosition += 1
                appearances = 2

            if nums[i] != actualNumber:
                nums[nextPosition] = nums[i]
                actualNumber = nums[i]
                appearances = 1
                nextPosition += 1

        return nextPosition
