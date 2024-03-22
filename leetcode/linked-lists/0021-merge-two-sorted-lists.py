# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# solution considering the edge case of the merged list being empty at the beginning
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        mergedList = None

        if list1 and list2:
            if list1.val <= list2.val:
                mergedList = list1.val
                list1 = list1.next
            else:
                mergedList = list2.val
                list2 = list2.next
        elif list1:
            mergedList = list1.val
            list1 = list1.next
        elif list2:
            mergedList = list2.val
            list2 = list2.next

        temp = mergedList
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        while list1 is not None:
            temp.next = list1
            temp = temp.next
            list1 = list1.next

        while list2 is not None:
            temp.next = list2
            temp = temp.next
            list2 = list2.next

        return mergedList


# create a dummy node at the beginning of the mergedList to remove edge case of empty list in the beginning
class Solution2:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        mergedList = ListNode(-101)
        temp = mergedList
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        if list1 is not None:
            temp.next = list1

        if list2 is not None:
            temp.next = list2

        return mergedList.next
