学习笔记

哈希表

映射

集合

树, 二叉树, 二叉搜索树
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def preorder(self, root):
  if root:
    self.traverse_path.append(root.val)
    self.preorder(root.left)
    self.preorder(root.right)
    
def inorder(self, root):
  if root:
    self.inorder(root.left)
    self.traverse_path.append(root.val)
    self.inorder(root.right)

def postorder(self, root):
  if root:
    self.postorder(root.left)
    self.postorder(root.right)
    self.traverse_path.append(root.val)

堆

二叉堆

图
