class Solution(object):
    def removeDuplicates(self, nums):
        actualNumber = nums[0]
        actualPosition = 1

        for i, n in enumerate(nums):
            if n != actualNumber:
                nums[actualPosition] = n
                actualNumber = n
                actualPosition += 1

        return actualPosition
