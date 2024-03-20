# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

# A subarray is a contiguous part of any given array.

# Example 1:

# Input:
# N = 4, K = 2
# Arr = [100, 200, 300, 400]
# Output:
# 700
# Explanation:
# Arr3  + Arr4 =700,
# which is maximum.
# Example 2:

# Input:
# N = 4, K = 4
# Arr = [100, 200, 300, 400]
# Output:
# 1000
# Explanation:
# Arr1 + Arr2 + Arr3 + Arr4 =1000,
# which is maximum.
# Your Task:

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= N <= 105
# 1 <= Arri <= 105
# 1 <= K <= N


from typing import List


# solved on my own, got to see after that this is basically the sliding window with fixed size algorithm
def maxSumContiguousSubarray(nums: List[int], k: int):
    left = 0
    right = 0

    sum = 0
    while right < len(nums) and right < k:
        sum += nums[right]
        right += 1

    maxSum = sum

    while right < len(nums):
        sum -= nums[left]
        left += 1

        sum += nums[right]
        right += 1

        if sum > maxSum:
            maxSum = sum

    return maxSum
