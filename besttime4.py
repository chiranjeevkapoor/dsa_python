class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2*k+1)] for _ in range(n+1)]
        curr = after = [0 for _ in range(2*k+1)]
        for index in range(n-1, -1, -1):
            for transNo in range(2*k-1, -1, -1):
                if transNo%2==0:
                    curr[transNo] = max(-prices[index]+ after[transNo+1], 0 + after[transNo])
                else:
                    curr[transNo] = max(prices[index]+ after[transNo+1], 0 + after[transNo])
            after = curr
        return after[0]
        

        
        