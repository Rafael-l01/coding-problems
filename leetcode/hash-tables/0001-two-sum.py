class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        remainings = {}
        for i, num in enumerate(nums):
            if num in remainings:
                position = remainings[num]
                return [i, position]

            remaining = target - num
            remainings[remaining] = i
