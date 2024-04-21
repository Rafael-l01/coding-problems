# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LL:
    def __init__(self):
        self.head = ListNode(-1)

    def appendFirst(self, val):
        newNode = ListNode(val)

        next = self.head.next

        self.head.next = newNode
        newNode.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        currentNode = l1
        n1 = ""
        while currentNode:
            n1 = str(currentNode.val) + n1
            currentNode = currentNode.next

        currentNode = l2
        n2 = ""
        while currentNode:
            n2 = str(currentNode.val) + n2
            currentNode = currentNode.next

        result = int(n1) + int(n2)
        result = str(result)

        listResult = LL()
        for char in result:
            listResult.appendFirst(char)

        return listResult.head.next
