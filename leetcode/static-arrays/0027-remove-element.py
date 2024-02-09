class Solution(object):
    def removeElement(self, nums, val):
        actualPosition = 0
        k = 0
        for n in nums:
            if n != val:
                nums[actualPosition] = n
                actualPosition += 1
                k += 1

        return k
