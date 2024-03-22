# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# considering that the list has head and tail pointers
class Solution:
    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        while temp is not None:
            after = temp.next

            temp.next = before
            before = temp
            temp = after


# considering list has just head pointer
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head
        before = None
        after = temp.next

        while temp is not None:
            after = temp.next

            temp.next = before
            before = temp
            temp = after

        head = before
        return head


# solution that works for any list size without checking if list is empty and considering list has just head pointer
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        before = None

        while temp is not None:
            after = temp.next

            temp.next = before
            before = temp
            temp = after

        head = before
        return head
