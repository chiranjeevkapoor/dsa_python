class Solution:
    def solve(self, index, arr, n, k, dp):
        if index == n:
            return 0
        if dp[index] != -1:
            return dp[index]
        maxAns = float('-inf')
        partitionLength = 0
        maxi = float('-inf')

        for j in range(index, min(n, index+k)):
            partitionLength +=1
            maxi = max(maxi, arr[j])
            partitionSum = partitionLength*maxi + self.solve(j+1, arr, n, k, dp)
            maxAns = max(maxAns, partitionSum)
        dp[index] = maxAns
        return maxAns
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1 for _ in range(n)]
        return self.solve(0, arr, n, k, dp)
        