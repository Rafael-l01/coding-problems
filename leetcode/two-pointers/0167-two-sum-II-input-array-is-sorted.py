from typing import List


# first solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []


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
