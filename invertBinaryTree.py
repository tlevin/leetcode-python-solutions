class Solution(object):
    def invertTree(self, root):
      """
        :type root: TreeNode
        :rtype: TreeNode
         """
        if root is None:
            return []
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
