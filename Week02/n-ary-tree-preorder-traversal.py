"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return
        visited, out = [root], []
        while visited:
            tmp = visited.pop()
            out.append(tmp.val)
            visited.extend(tmp.children[::-1])
        return out

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         out = []
#         def pre(node):
#             if not node: return []
#             out.append(node.val)
#             for i in node.children:
#                 pre(i)
#         pre(root)
#         return out
