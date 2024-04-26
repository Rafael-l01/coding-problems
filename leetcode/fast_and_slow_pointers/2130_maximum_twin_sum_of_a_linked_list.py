# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.


# Example 1:


# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6.
# Example 2:


# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
# Example 3:


# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.


# Constraints:

# The number of nodes in the list is an even integer in the range [2, 105].
# 1 <= Node.val <= 105


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# first solution, O(n) time complexity and O(n) space complexity
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []

        cur = head
        while cur:
            array.append(cur.val)
            cur = cur.next

        left = 0
        right = len(array) - 1

        maxSum = 0
        while left <= right:
            sum = array[left] + array[right]
            maxSum = max(maxSum, sum)

            left += 1
            right -= 1

        return maxSum


# second solution, O(n) time complexity and O(1) space complexity
class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        before = None

        # reverse first half of the list
        while fast and fast.next:
            fast = fast.next.next

            after = slow.next
            slow.next = before

            before = slow
            slow = after

        firstHalf = before
        secondHalf = slow

        maxSum = 0
        while firstHalf:
            sum = firstHalf.val + secondHalf.val
            maxSum = max(maxSum, sum)

            firstHalf = firstHalf.next
            secondHalf = secondHalf.next

        return maxSum
