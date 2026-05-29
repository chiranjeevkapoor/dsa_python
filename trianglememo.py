class Solution:
    def solve(self, i, j, triangle, n, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        if i == n-1:
            return triangle[i][j]
        d = self.solve(i+1, j, triangle, n, dp)
        dg = self.solve(i+1, j+1, triangle, n, dp)
        dp[i][j] = triangle[i][j] + min(d, dg)

        return dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.solve(0, 0, triangle, n, dp)
        