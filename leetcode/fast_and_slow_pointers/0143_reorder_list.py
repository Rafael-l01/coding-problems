# 143. Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# slow and fast pointer, O(n) time complexity, O(1) space complexity
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle element of list
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half of list
        prev = None
        while slow:
            next = slow.next
            slow.next = prev

            prev = slow
            slow = next

        # merge the two halfs
        secondHalf = prev
        firstHalf = head
        while secondHalf != firstHalf and firstHalf.next != secondHalf:
            next = firstHalf.next
            firstHalf.next = secondHalf

            secondHalf = secondHalf.next
            firstHalf = firstHalf.next
            firstHalf.next = next
            firstHalf = firstHalf.next


# second solution using O(n) space complexity and O(n) time complexity
class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            nodes[right].next = nodes[left + 1]

            left += 1
            right -= 1

        nodes[left].next = None
