class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N, count = len(M), 0
        queue, visited = [], [0]*N
        for i in range(N):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    tmp = queue.pop(0)                    
                    for j in range(N):
                        if M[tmp][j] == 1 and visited[j] == 0:
                            visited[j] = 1
                            queue.append(j)                            
                count += 1
        return count
