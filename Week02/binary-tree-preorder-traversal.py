# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                res.append(root.val)
                if root.left: helper(root.left)
                if root.right: helper(root.right)
        helper(root)
        return res
