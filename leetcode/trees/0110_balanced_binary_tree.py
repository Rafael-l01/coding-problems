# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true


# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def dfs(currentNode):
            if currentNode is None:
                return 0

            leftHeight = dfs(currentNode.left)
            rightHeight = dfs(currentNode.right)

            if abs(leftHeight - rightHeight) > 1:
                balanced[0] = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return balanced[0]


# different way of handling the balanced variable
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(currentNode):
            if currentNode is None:
                return {"isBalanced": True, "height": 0}

            left, right = dfs(currentNode.left), dfs(currentNode.right)

            balanced = (
                left["isBalanced"]
                and right["isBalanced"]
                and abs(left["height"] - right["height"]) <= 1
            )

            return {
                "isBalanced": balanced,
                "height": 1 + max(left["height"], right["height"]),
            }

        return dfs(root)["isBalanced"]
