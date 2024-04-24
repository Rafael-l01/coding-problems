# 543. Diameter of Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first solution, O(n^2) time complexity
class Solution:
    def depthOfTree(self, currentNode):
        if currentNode is None:
            return 0

        return 1 + max(
            self.depthOfTree(currentNode.left), self.depthOfTree(currentNode.right)
        )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        allNodes = []

        def traverse(currentNode):
            if currentNode is None:
                return None

            allNodes.append(currentNode)

            traverse(currentNode.left)

            traverse(currentNode.right)

        traverse(root)

        biggestDiameter = 0
        for node in allNodes:
            depthLeftSubTree = self.depthOfTree(node.left)
            depthRightSubTree = self.depthOfTree(node.right)

            diameter = depthLeftSubTree + depthRightSubTree
            biggestDiameter = max(biggestDiameter, diameter)

        return biggestDiameter


# second solution with O(n) time complexity
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        biggestDiameter = [0]

        def dfs(currentNode):
            if currentNode is None:
                return -1

            leftHeight = dfs(currentNode.left)
            rightHeight = dfs(currentNode.right)

            diameter = (leftHeight + 1) + (rightHeight + 1)
            biggestDiameter[0] = max(biggestDiameter[0], diameter)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return biggestDiameter[0]
