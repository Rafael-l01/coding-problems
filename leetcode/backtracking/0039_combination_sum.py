# 39. Combination Sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []


# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

from typing import List


# using "pure" backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allComb = []

        def backtrack(start, comb, sumComb):
            if sumComb > target:
                return

            if sumComb == target:
                allComb.append(comb.copy())
                return

            for i in range(start, len(candidates)):
                if sumComb + candidates[i] <= target:
                    comb.append(candidates[i])
                    backtrack(i, comb, sumComb + candidates[i])

                    comb.pop()

        backtrack(0, [], 0)
        return allComb


# using dfs in space state tree, time complexity O(2^target) for each node in state space tree we have 2 options, and the height of tree is at max target
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allComb = []

        def backtrack(i, comb, sumComb):
            if sumComb > target:
                return

            if sumComb == target:
                allComb.append(comb.copy())
                return

            if i == len(candidates):
                return

            comb.append(candidates[i])
            backtrack(i, comb, sumComb + candidates[i])

            comb.pop()
            backtrack(i + 1, comb, sumComb)

        backtrack(0, [], 0)
        return allComb
