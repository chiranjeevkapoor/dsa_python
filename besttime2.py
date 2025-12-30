class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        aheadbuy = aheadnotbuy = 0
        for index in range(n-1, -1,-1):
            currnotbuy = max(prices[index]+aheadbuy , 0+ aheadnotbuy)
            currbuy = max(-prices[index]+aheadnotbuy, 0 + aheadbuy)

            aheadbuy = currbuy
            aheadnotbuy = currnotbuy
        return aheadbuy



        