# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# first solution
class Stack:
    def __init__(self):
        self.stack = []
        self.height = 0

    def push(self, value):
        self.stack.append(value)
        self.height += 1

    def pop(self):
        if self.isEmpty():
            return None

        self.height -= 1
        return self.stack.pop()

    def isEmpty(self):
        return self.height == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.push(char)

            if char == ")" and stack.pop() != "(":
                return False

            if char == "]" and stack.pop() != "[":
                return False

            if char == "}" and stack.pop() != "{":
                return False

        if not stack.isEmpty():
            return False

        return True


# second solution
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in closeToOpen:
                if not stack or stack.pop() != closeToOpen[char]:
                    return False
            else:
                stack.append(char)

        if len(stack) != 0:
            return False

        return True
