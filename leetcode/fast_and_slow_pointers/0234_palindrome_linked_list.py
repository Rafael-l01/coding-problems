# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.


# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false


# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9


# Follow up: Could you do it in O(n) time and O(1) space?

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity O(n) and space complexity O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        cur = head

        while cur:
            nodes.append(cur.val)
            cur = cur.next

        left = 0
        right = len(nodes) - 1
        while left <= right:
            if nodes[left] != nodes[right]:
                return False

            left += 1
            right -= 1

        return True


# time complexity O(n) and space complexity O(1), using slow and fast pointers
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow, fast = head, head
        prev = None
        size = 1

        while fast and fast.next:
            fast = fast.next.next
            size += 2

            next = slow.next
            slow.next = prev

            prev = slow
            slow = next

        if not fast:
            size -= 1

        firstHalf = prev

        if size % 2 == 0:
            secondHalf = slow
        else:
            secondHalf = slow.next

        while firstHalf:
            if firstHalf.val != secondHalf.val:
                return False

            firstHalf = firstHalf.next
            secondHalf = secondHalf.next

        return True


# time complexity O(n) and space complexity O(1), using slow and fast pointers, but now reversing the second half of the list
class Solution3:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        secondHalf = prev

        while secondHalf:
            if head.val != secondHalf.val:
                return False

            head = head.next
            secondHalf = secondHalf.next

        return True
