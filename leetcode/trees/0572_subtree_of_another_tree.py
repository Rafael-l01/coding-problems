# 572. Subtree of Another Tree

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false


# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first solution
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodesEqualsSubRoot = []

        def findNode(currentTreeNode, subTreeNode):
            if not currentTreeNode:
                return None

            if currentTreeNode.val == subTreeNode.val:
                nodesEqualsSubRoot.append(currentTreeNode)

            findNode(currentTreeNode.left, subTreeNode)
            findNode(currentTreeNode.right, subTreeNode)

        def sameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        subTree = findNode(root, subRoot)

        for node in nodesEqualsSubRoot:
            if sameTree(node, subRoot):
                return True

        return False


# second solution, time complexity O(n * m), considering n the number of nodes in root and m the number of nodes in subRoot
class Solution2:
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(
            root.right, subRoot.right
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
