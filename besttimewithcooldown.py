class Solution:
    def solve(self, index, buy, prices, n, dp):
        if index>=n:
            return 0
        if dp[index][buy]!=-1:
            return dp[index][buy]
        if buy:
            dp[index][buy] = max(-prices[index]+self.solve(index+1, 0, prices ,n, dp),
            0 + self.solve(index+1, 1, prices, n, dp))
            return dp[index][buy]
        else:
            dp[index][buy] = max(prices[index]+self.solve(index+2, 1, prices, n, dp),
            0 + self.solve(index+1, 0, prices, n, dp))
            return dp[index][buy]
            
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+2)]

        for index in range(n-1, -1, -1):
                
            dp[index][1] = max(-prices[index]+dp[index+1][0], 0 + dp[index+1][1])
                
            dp[index][0] = max(prices[index]+dp[index+2][1], 0 + dp[index+1][0])
        return dp[0][1]
        
        