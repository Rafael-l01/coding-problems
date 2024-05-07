# 78. Subsets

# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(subset, nextChoices):
            if len(nextChoices) == 0:
                subsets.append(subset.copy())
                return

            subset.append(nextChoices[0])
            backtrack(subset, nextChoices[1:])

            subset.pop()
            backtrack(subset, nextChoices[1:])

        backtrack([], nums)
        return subsets


# dfs on state space tree, time complexity O(n*2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []

        subset = []

        def dfs(i):
            if i == len(nums):
                allSubsets.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to exclude num[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return allSubsets


# backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []

        subset = []

        def backtrack(start):
            allSubsets.append(subset.copy())

            for index in range(start, len(nums)):
                # include number
                subset.append(nums[index])
                backtrack(index + 1)

                # exclude number
                subset.pop()

        backtrack(0)
        return allSubsets
