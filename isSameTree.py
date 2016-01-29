class Solution(object):
    def isSameTree(self, p, q):
      """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
         """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        solution = left and self.isSameTree(p.right, q.right)
        return solution
