# 47. Permutations II

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

import collections
from typing import List


# time complexity O(n * n * n!), space complexity O(n*n! + n) considering result array, if not O(n) for call stack
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        allPermutations = []

        def backtrack(permutation, used):
            if len(permutation) == len(nums):
                allPermutations.append(permutation.copy())
                return

            usedNumsIteration = []
            for i in range(len(nums)):
                if used[i] == False and nums[i] not in usedNumsIteration:
                    permutation.append(nums[i])
                    used[i] = True
                    backtrack(permutation, used)

                    permutation.pop()
                    used[i] = False
                    usedNumsIteration.append(nums[i])

        usedNums = [False] * len(nums)
        backtrack([], usedNums)
        return allPermutations


# time complexity O(n * n!), space complexity O(n*n! + n) considering result array, if not O(n) for call stack
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        allPermutations = []
        mapDifferentNums = collections.defaultdict(int)
        for num in nums:
            mapDifferentNums[num] += 1

        def backtrack(permutation):
            if len(permutation) == len(nums):
                allPermutations.append(permutation.copy())
                return

            for num, count in mapDifferentNums.items():
                if count > 0:
                    permutation.append(num)
                    mapDifferentNums[num] -= 1

                    backtrack(permutation)

                    permutation.pop()
                    mapDifferentNums[num] += 1

        backtrack([])
        return allPermutations
