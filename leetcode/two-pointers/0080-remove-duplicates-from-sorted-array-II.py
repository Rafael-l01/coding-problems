# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


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
