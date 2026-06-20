class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        after = curr = [0 for _ in range(5)]
        for index in range(n-1, -1, -1):
            for transaction in range(3, -1, -1):
                if transaction%2==0:
                    curr[transaction] = max(-prices[index] + after[transaction+1],
                                                0 + after[transaction])
                else:
                    curr[transaction] = max(prices[index] + after[transaction+1],
                                                0 + after[transaction])
            after = curr
        return after[0]



        

        