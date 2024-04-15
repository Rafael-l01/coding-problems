# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        currentNode = root
        level = 0
        queue = [[currentNode, level]]
        result = []

        while len(queue) > 0:
            currentNode, level = queue.pop(0)

            if len(result) > level:
                result[level].append(currentNode.val)
            else:
                result.append([currentNode.val])

            if currentNode.left is not None:
                queue.append([currentNode.left, level + 1])

            if currentNode.right is not None:
                queue.append([currentNode.right, level + 1])

        return result


# second solution
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []

        queue = collections.deque()
        queue.append(root)

        while len(queue) > 0:
            queueLen = len(queue)
            level = []

            for i in range(queueLen):
                currentNode = queue.popleft()
                level.append(currentNode.val)

                if currentNode.left is not None:
                    queue.append(currentNode.left)

                if currentNode.right is not None:
                    queue.append(currentNode.right)

            result.append(level)

        return result
