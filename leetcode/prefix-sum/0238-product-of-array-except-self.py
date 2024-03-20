# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List


# first time solution
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])

        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        answer = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = postfix[i + 1]
                continue

            if i == len(nums) - 1:
                answer[i] = prefix[i - 1]
                continue

            answer[i] = prefix[i - 1] * postfix[i + 1]

        return answer


# second time solution using O(1) space complexity (the problem says to disconsider the answer array in the space complexity)
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefixProduct = 1
        for i in range(len(nums) - 1):
            prefixProduct *= nums[i]
            answer[i + 1] *= prefixProduct

        postfixProduct = 1
        for i in range(len(nums) - 1, 0, -1):
            postfixProduct *= nums[i]
            answer[i - 1] *= postfixProduct

        return answer
