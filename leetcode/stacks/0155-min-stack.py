# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


# solution using array
class MinStack:

    def __init__(self):
        self.stack = []
        self.height = 0
        self.min = 2**31

    def push(self, val: int) -> None:
        self.min = val if self.min > val else self.min

        self.stack.append({"value": val, "min": self.min})
        self.height += 1

    def pop(self) -> None:
        self.stack.pop()
        self.height -= 1

        if self.stack:
            self.min = self.stack[-1]["min"]
        else:
            self.min = 2**31

    def top(self) -> int:
        return self.stack[-1]["value"]

    def getMin(self) -> int:
        return self.min


# solution using linked list
class Node:
    def __init__(self, value: int, min: int):
        self.value = value
        self.min = min
        self.next = None


class MinStackLinkedList:

    def __init__(self):
        self.topNode = None
        self.height = 0
        self.min = 2**31

    def push(self, val: int) -> None:
        self.min = val if self.min > val else self.min

        newNode = Node(val, self.min)
        newNode.next = self.topNode
        self.topNode = newNode

        self.height += 1

    def pop(self) -> None:
        temp = self.topNode
        self.topNode = self.topNode.next
        temp.next = None

        self.height -= 1

        if self.topNode:
            self.min = self.topNode.min
        else:
            self.min = 2**31

    def top(self) -> int:
        return self.topNode.value

    def getMin(self) -> int:
        return self.min
