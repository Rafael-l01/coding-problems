# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


# Constraints:


# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# solution using BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = collections.deque()
        queue.append(root)
        numLevels = 0

        while len(queue) > 0:
            numLevels += 1
            for i in range(len(queue)):
                currentNode = queue.popleft()

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

        return numLevels


# solution using recursive DFS
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# solution using iterative DFS
class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]
        maxDepth = 1

        while stack:
            currentNode, depth = stack.pop()

            if currentNode:
                if maxDepth < depth:
                    maxDepth = depth

                stack.append((currentNode.right, depth + 1))
                stack.append((currentNode.left, depth + 1))

        return maxDepth
