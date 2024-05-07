# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]


# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


from typing import List


# time complexity O(n*2^n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        allComb = []

        def backtrack(i, comb, sumComb):
            if sumComb == target:
                allComb.append(comb.copy())
                return

            if sumComb > target:
                return

            if i == len(candidates):
                return

            comb.append(candidates[i])
            backtrack(i + 1, comb, sumComb + candidates[i])

            comb.pop()
            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i + 1, comb, sumComb)

        backtrack(0, [], 0)
        return allComb
