# 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        currentNode = head
        listLength = 1
        while currentNode.next:
            listLength += 1
            currentNode = currentNode.next

        rotations = k % listLength
        if rotations == 0:
            return head

        currentNode.next = head

        currentNode = head
        for i in range(listLength - rotations - 1):
            currentNode = currentNode.next

        newHead = currentNode.next
        currentNode.next = None

        return newHead
