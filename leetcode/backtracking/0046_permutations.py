# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPermutations = []

        def backtrack(permutation):
            if len(permutation) == len(nums):
                allPermutations.append(permutation.copy())
                return

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack(permutation)

                    permutation.pop()

        backtrack([])
        return allPermutations


# using used list, instead of O(n) count operation to check if number was already used
# time complexity O(n*n!), space complexity O(n*n!) considering result array, if not O(n) for call stack
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPermutations = []

        def backtrack(permutation, used):
            if len(permutation) == len(nums):
                allPermutations.append(permutation.copy())
                return

            for i in range(len(nums)):
                if used[i] == False:
                    permutation.append(nums[i])
                    used[i] = True
                    backtrack(permutation, used)

                    permutation.pop()
                    used[i] = False

        usedNums = [False] * len(nums)
        backtrack([], usedNums)
        return allPermutations
