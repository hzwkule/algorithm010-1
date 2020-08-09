class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited, queue = [0] * len(M), []
        count = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1
        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)

    


                
                        
