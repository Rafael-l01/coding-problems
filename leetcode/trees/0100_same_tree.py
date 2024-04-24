# 100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false


# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(currentNode, nodesVisited):
            if currentNode is None:
                nodesVisited.append(None)
                return nodesVisited

            nodesVisited.append(currentNode.val)

            dfs(currentNode.left, nodesVisited)
            dfs(currentNode.right, nodesVisited)

            return nodesVisited

        pTree = dfs(p, [])
        qTree = dfs(q, [])

        return pTree == qTree


# second solution, time complexity of O(p + q), considering it the size of each tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)