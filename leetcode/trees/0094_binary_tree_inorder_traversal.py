# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
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
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        def traversal(currentNode):
            if currentNode.left:
                traversal(currentNode.left)

            results.append(currentNode.val)

            if currentNode.right:
                traversal(currentNode.right)

        if root:
            traversal(root)

        return results


# first time iterative solution
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        results = []

        queue = collections.deque()
        queue.append(root)

        visited = collections.deque()

        while len(queue) > 0:
            currentNode = queue.popleft()

            if len(visited) > 0 and visited[0] == currentNode.val:
                visited.popleft()
                results.append(currentNode.val)
                continue
            else:
                visited.appendleft(currentNode.val)

            if currentNode.right:
                queue.appendleft(currentNode.right)

            queue.appendleft(currentNode)

            if currentNode.left:
                queue.appendleft(currentNode.left)

        return results


# second iterative solution
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        currentNode = root
        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            currentNode = stack.pop()
            result.append(currentNode.val)
            currentNode = currentNode.right

        return result
