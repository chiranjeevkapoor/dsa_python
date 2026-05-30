#User function Template for python3
class Solution:
    def maximumPath(self, mat):
        n = len(mat)
        m = len(mat[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i==0:
                    dp[i][j] = mat[i][j]
                else:
                    up = upleft = upright = float("-inf")
                    if j>0:
                        upleft = dp[i-1][j-1]
                    up = dp[i-1][j]
                    if j<m-1:
                        upright = dp[i-1][j+1]
                    dp[i][j] = mat[i][j] + max(up, upleft, upright)
        
        return max(dp[n-1])

        
            