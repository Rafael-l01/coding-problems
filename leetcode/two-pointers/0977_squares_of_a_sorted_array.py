# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

from typing import List


# trivial solution, time complexity 0(nlogn) because of sorting
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        nums.sort()
        return nums


# second solution with O(n) time complexity and O(n) space complexity
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negativeNumbers = -1
        positiveNumbers = 0

        while positiveNumbers < len(nums) and nums[positiveNumbers] < 0:
            positiveNumbers += 1
            negativeNumbers += 1

        squares = []
        while positiveNumbers < len(nums) and negativeNumbers > -1:
            if abs(nums[positiveNumbers]) <= abs(nums[negativeNumbers]):
                squares.append(nums[positiveNumbers] ** 2)
                positiveNumbers += 1
            else:
                squares.append(nums[negativeNumbers] ** 2)
                negativeNumbers -= 1

        while positiveNumbers < len(nums):
            squares.append(nums[positiveNumbers] ** 2)
            positiveNumbers += 1

        while negativeNumbers > -1:
            squares.append(nums[negativeNumbers] ** 2)
            negativeNumbers -= 1

        return squares


# third solution, with O(n) time complexity and O(n) space complexity
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        squares = []
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                squares.append(nums[left] ** 2)
                left += 1
            else:
                squares.append(nums[right] ** 2)
                right -= 1

        return squares[::-1]
