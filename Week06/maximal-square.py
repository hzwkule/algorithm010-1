class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
        return len(matrix) and max(map(max, matrix)) ** 2
