class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:        
        # m, n = len(grid), len(grid[0])
        # dp = m*[n*[0]]
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if i == m-1 and j == n-1:
        #             dp[i][j] = grid[i][j]
        #         elif i == m-1:
        #             dp[i][j] = dp[i][j+1] + grid[i][j]
        #         elif j == n-1:
        #             dp[i][j] = dp[i+1][j] + grid[i][j]
        #         else:
        #             dp[i][j] = min(dp[i][j+1], dp[i+1][j]) + grid[i][j]
        # return dp[0][0]
        m, n = len(grid), len(grid[0])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    grid[i][j] = grid[i][j]
                elif i == m-1:
                    grid[i][j] = grid[i][j+1] + grid[i][j]
                elif j == n-1:
                    grid[i][j] = grid[i+1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j+1], grid[i+1][j]) + grid[i][j]
        return grid[0][0]
