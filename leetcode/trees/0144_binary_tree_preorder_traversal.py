# 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traversal(currentNode):
            result.append(currentNode.val)

            if currentNode.left:
                traversal(currentNode.left)

            if currentNode.right:
                traversal(currentNode.right)

        if root:
            traversal(root)

        return result


# iterative solution
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        currentNode = root
        while currentNode or stack:
            while currentNode:
                result.append(currentNode.val)
                stack.append(currentNode)
                currentNode = currentNode.left

            currentNode = stack.pop()
            currentNode = currentNode.right

        return result


# second iterative solution
class Solution3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        currentNode = root
        while currentNode or stack:
            if currentNode:
                result.append(currentNode.val)
                stack.append(currentNode.right)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()

        return result
