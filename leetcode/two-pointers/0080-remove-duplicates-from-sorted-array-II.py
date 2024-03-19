from typing import List


# first solution
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


# second solution
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        actualNumber = nums[left]

        while right < len(nums):
            counter = 0
            while right < len(nums) and nums[right] == actualNumber:
                if counter < 2:
                    counter += 1
                right += 1

            for i in range(counter):
                nums[left] = actualNumber
                left += 1

            if right < len(nums):
                actualNumber = nums[right]

        return left


# third solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0

        while right < len(nums):
            counter = 1
            while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                if counter < 2:
                    counter += 1
                right += 1

            for i in range(counter):
                nums[left] = nums[right]
                left += 1

            right += 1

        return left
