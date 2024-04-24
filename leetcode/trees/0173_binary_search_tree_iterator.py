# 173. Binary Search Tree Iterator

# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.


# Example 1:


# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False


# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 0 <= Node.val <= 106
# At most 105 calls will be made to hasNext, and next.


# Follow up:

# Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# next and hasNext operations have time complexity of O(n) and space complexity of 0(n), considering n number of nodes of tree
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iterator = -1

    def inOrderTraversal(self, root, lastNode):
        if root is None:
            return None

        nodeLeft = self.inOrderTraversal(root.left, lastNode)
        if nodeLeft:
            return nodeLeft

        if root.val > lastNode:
            return root

        return self.inOrderTraversal(root.right, lastNode)

    def next(self) -> int:
        nextNode = self.inOrderTraversal(self.root, self.iterator)
        self.iterator = nextNode.val
        return self.iterator

    def hasNext(self) -> bool:
        nextNode = self.inOrderTraversal(self.root, self.iterator)
        return True if nextNode else False


# second solution, next and hasNext operations have time complexity of O(1),
# but constructor has time complexity of O(n)
# and space complexity is 0(n), considering n number of nodes of tree
# as we have an array with all nodes of the tree in order
class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nodesInOrder = []
        self.inOrderTraversal(self.root)
        self.iterator = -1

    def inOrderTraversal(self, root):
        if root is None:
            return None

        self.inOrderTraversal(root.left)
        self.nodesInOrder.append(root.val)
        self.inOrderTraversal(root.right)

    def next(self) -> int:
        self.iterator += 1
        return self.nodesInOrder[self.iterator]

    def hasNext(self) -> bool:
        nextNode = self.iterator + 1
        return nextNode < len(self.nodesInOrder)


# third solution, the space complexity in here is O(log n) or O(height of tree)
# but the time complexity is in AVERAGE O(1)
class BSTIterator3:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        res = self.stack.pop()

        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
