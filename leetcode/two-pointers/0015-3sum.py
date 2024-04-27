# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


from collections import defaultdict
from typing import List


# naive approach, O(n^3) time complexity
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        result.add(tuple(triplet))

        return result


# fix one number, and solve two sum problem with rest of array for each fixed i, achieving O(n^2) time complexity and O(n) space complexity
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) - 2):
            remainings = defaultdict()
            for j in range(i + 1, len(nums)):
                if nums[j] in remainings:
                    k = remainings[nums[j]]
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()
                    result.add(tuple(triplet))
                else:
                    remaining = 0 - (nums[i] + nums[j])
                    remainings[remaining] = j

        return result


# fix one number, and use two pointer technique to achieve O(nlogn + n^2) time complexity and O(1) space complexity
class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    result.add(tuple([nums[left], nums[right], nums[i]]))
                    left += 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


# this solution is same as third, but don't consider duplicates for first position when looping through the array
# and for the left and right pointer, so, in this case we don't need to use a set to save the results,
# and don't need to convert the triplets to tuples to add to set, so is more effective because of it too
class Solution4:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
