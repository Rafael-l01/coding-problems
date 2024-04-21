# 230. Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104


# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        orderedValues = []

        def traverse(currentNode):
            if currentNode.left:
                traverse(currentNode.left)

            orderedValues.append(currentNode.val)

            if currentNode.right:
                traverse(currentNode.right)

        if root:
            traverse(root)

        return orderedValues[k - 1]


# considering the tree can have an attribute in each node that says how many descendants it has
# we can find the k-th smallest element in O(log n) / O(height of tree) time complexity
class TreeNode2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.numDescendants = 1


class BST:
    def __init__(self):
        self.root = None

    def __insert(self, currentNode, value):
        if currentNode == None:
            return TreeNode2(value)

        if value < currentNode.val:
            currentNode.left = self.__insert(currentNode.left, value)

        if value > currentNode.val:
            currentNode.right = self.__insert(currentNode.right, value)

        currentNode.numDescendants += 1

        return currentNode

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    # used just to check the created tree
    def bfsWithLevelDivision(self):
        if self.root is None:
            return []

        result = []

        queue = collections.deque()
        queue.append(self.root)

        while len(queue) > 0:
            queueLength = len(queue)
            level = []

            for i in range(queueLength):
                currentNode = queue.popleft()
                level.append((currentNode.val, currentNode.numDescendants))

                if currentNode.left is not None:
                    queue.append(currentNode.left)

                if currentNode.right is not None:
                    queue.append(currentNode.right)

            result.append(level)

        return result


# solve it iteratively, time complexity is O(height of the tree), space complexity O(1)
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode2], k: int) -> int:
        currentNode = root
        jumpedNodes = 0

        while currentNode:
            if currentNode.left is None:
                leftDescendants = 0 + jumpedNodes
            else:
                leftDescendants = currentNode.left.numDescendants + jumpedNodes

            if leftDescendants >= k:
                currentNode = currentNode.left
            else:
                if leftDescendants + 1 == k:
                    return currentNode.val
                else:
                    jumpedNodes = leftDescendants + 1
                    currentNode = currentNode.right

        return None


# solve it recursively, time complexity is O(height of the tree), space complexity O(height of the tree)
class Solution3:
    def kthSmallest(self, root: Optional[TreeNode2], k: int, jumpedNodes: int) -> int:
        if root is None:
            return None

        if root.left is None:
            leftDescendants = 0
        else:
            leftDescendants = root.left.numDescendants

        if jumpedNodes + leftDescendants >= k:
            return self.kthSmallest(root.left, k, jumpedNodes)
        else:
            if jumpedNodes + leftDescendants + 1 == k:
                return root.val
            else:
                return self.kthSmallest(
                    root.right, k, jumpedNodes + leftDescendants + 1
                )


bst = BST()

bst.insert(81)
bst.insert(44)
bst.insert(122)
bst.insert(22)
bst.insert(63)
bst.insert(101)
bst.insert(141)
bst.insert(10)
bst.insert(31)
bst.insert(55)
bst.insert(72)
bst.insert(94)

print(bst.bfsWithLevelDivision())

s2 = Solution2()
print(s2.kthSmallest(bst.root, 13))
