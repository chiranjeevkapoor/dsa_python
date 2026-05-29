class Solution:
    def solve(self, m, n, dp):
        if m == 0 or n == 0:
            return 1
        if dp[m][n] != -1:
            return dp[m][n]
        left = self.solve(m, n-1, dp)
        up = self.solve(m-1, n, dp)
        dp[m][n] = left + up
        return left + up


    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = left = 0
                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left
        
        return dp[m-1][n-1]
