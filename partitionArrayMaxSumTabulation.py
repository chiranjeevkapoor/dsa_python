class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n+1)]
        
        for index in range(n-1, -1, -1):
            maxAns = float('-inf')
            partitionLength = 0
            maxi = float('-inf')

            for j in range(index, min(n, index+k)):
                partitionLength +=1
                maxi = max(maxi, arr[j])
                partitionSum = maxi*partitionLength + dp[j+1]
                maxAns = max(maxAns, partitionSum)
            dp[index] = maxAns
        return dp[0]

         