# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

from typing import List


# brute force solution, time complexity O(n^2)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (abs(i - j) <= k):
                    return True

        return False


# using "sliding window" as brute force, time complexity O(n*k), space complexity O(1)
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        for i in range(len(nums) - 1):
            # want to stop at i+k
            j = i + 1
            while j < len(nums) and j <= i + k:
                if nums[i] == nums[j]:
                    return True

                j += 1

        return False


# using a hashmap to map duplicates, time complexity O(n), space complexity O(n)
class Solution3:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                if i - map[nums[i]] <= k:
                    return True

                map[nums[i]] = i
            else:
                map[nums[i]] = i

        return False


# using sliding window and a hashset, time complexity O(n), space complexity O(k) that in the worst case is O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])

        return False
