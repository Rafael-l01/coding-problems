# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.


# Example 1:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:

# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


# Constraints:
# 1 <= arr.length <= 105
# 1 <= arr[i] <= 104
# 1 <= k <= arr.length
# 0 <= threshold <= 104


from typing import List


# time complexity O(n) and space complexity O(1)
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        numSubArrays = 0

        currentSum = 0
        for right in range(len(arr)):
            currentSum += arr[right]

            if right - left >= (k - 1):
                avg = currentSum / k
                if avg >= threshold:
                    numSubArrays += 1

                currentSum -= arr[left]
                left += 1

        return numSubArrays


# second solution, same complexities just different ways of handling sliding window
class Solution2:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        numSubArrays = 0
        currentSum = sum(arr[: k - 1])

        for left in range(len(arr) - k + 1):
            currentSum += arr[left + k - 1]

            if (currentSum / k) >= threshold:
                numSubArrays += 1

            currentSum -= arr[left]

        return numSubArrays
