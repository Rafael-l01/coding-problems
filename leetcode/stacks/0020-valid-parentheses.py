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
