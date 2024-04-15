# 145. Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]


# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive soltion
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(currentNode):
            if currentNode.left:
                traverse(currentNode.left)

            if currentNode.right:
                traverse(currentNode.right)

            result.append(currentNode.val)

        if root:
            traverse(root)

        return result


# iterative solution
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        currentNode = root

        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            currentNode = stack.pop()
            if currentNode.right is None or (
                len(result) > 0 and result[-1] == currentNode.right.val
            ):
                result.append(currentNode.val)
                currentNode = None
            else:
                stack.append(currentNode)
                currentNode = currentNode.right

        return result


# second iterative solution
class Solution3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]

        result = []

        while stack:
            currentNode, visited = stack.pop(), visit.pop()

            if currentNode:
                if visited:
                    result.append(currentNode.val)
                else:
                    stack.append(currentNode)
                    visit.append(True)

                    stack.append(currentNode.right)
                    visit.append(False)

                    stack.append(currentNode.left)
                    visit.append(False)

        return result
