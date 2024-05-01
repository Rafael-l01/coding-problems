# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
from typing import List


# first try doing the variable size sliding window, time complexity O(n), space complexity O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        currentSum = 0
        minLen = len(nums) + 1

        while right < len(nums):
            currentSum += nums[right]

            if currentSum >= target:
                minLen = min(minLen, (right - left) + 1)

                while left <= right and currentSum >= target:
                    minLen = min(minLen, (right - left) + 1)

                    if minLen == 1:
                        return minLen

                    currentSum -= nums[left]
                    left += 1

            right += 1

        if minLen == len(nums) + 1:
            return 0

        return minLen


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        minLen = len(nums) + 1

        left = 0
        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum >= target:
                minLen = min(minLen, (right - left) + 1)

                if minLen == 1:
                    return minLen

                currentSum -= nums[left]
                left += 1

        return 0 if minLen == len(nums) + 1 else minLen


# the solutions just work because the arrays have just positive numbers, if it had negative numbers, it wouldn't work


# third solution using binary search and prefix sum, for the follow up question, time complexity O(nlogn), space complexity O(n)
class Solution3:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum = [0] * (len(nums) + 1)

        for i, num in enumerate(nums):
            prefixSum[i + 1] = prefixSum[i] + num

        minLen = len(nums) + 1
        for i in range(len(nums)):
            left, right = i, len(prefixSum) - 1
            while left <= right:
                middle = left + ((right - left) // 2)
                actualPrefix = prefixSum[middle] - prefixSum[i]

                if actualPrefix >= target:
                    minLen = min(minLen, (middle - 1) - i + 1)

                    if minLen == 1:
                        return 1

                    right = middle - 1
                else:
                    left = middle + 1

        return 0 if minLen == len(nums) + 1 else minLen
