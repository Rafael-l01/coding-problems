from typing import List


# first time solution
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])

        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        answer = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = postfix[i + 1]
                continue

            if i == len(nums) - 1:
                answer[i] = prefix[i - 1]
                continue

            answer[i] = prefix[i - 1] * postfix[i + 1]

        return answer


# second time solution using O(1) space complexity (the problem says to disconsider the answer array in the space complexity)
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefixProduct = 1
        for i in range(len(nums) - 1):
            prefixProduct *= nums[i]
            answer[i + 1] *= prefixProduct

        postfixProduct = 1
        for i in range(len(nums) - 1, 0, -1):
            postfixProduct *= nums[i]
            answer[i - 1] *= postfixProduct

        return answer
