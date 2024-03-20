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
