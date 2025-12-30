class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        profit = 0
        for s in range(1, n):
            cost = prices[s] - mini
            profit = max(profit, cost)
            mini = min(mini, prices[s])
        
        
        return profit


        