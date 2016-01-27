# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
      """
        :type root: TreeNode
        :rtype: int
         """
        self.maxDepth = 0
        def traverseTree(node, depth):
            if node is None:
              return
            if node.left is None and node.right is None:
                self.maxDepth = max(self.maxDepth, depth)
                return
            else:
                if node.left:
                    traverseTree(node.left, depth+1)
                if node.right:
                    traverseTree(node.right, depth+1)
        traverseTree(root, 1)
        return self.maxDepth
