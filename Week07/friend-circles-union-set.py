class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(parent, i, j)
        return len(set([self._parent(parent, i) for i in range(n)]))

    def _union(self, parent, i, j):
        parent_i = self._parent(parent, i)
        parent_j = self._parent(parent, j)
        parent[parent_i] = parent_j

    def _parent(self, parent, i):
        root = i
        while parent[root] != root:
            root = parent[root]
        while parent[i] != i:
            tmp = i; i = parent[i]; parent[i] = root
        return root

