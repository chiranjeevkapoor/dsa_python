class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1 for _ in range(n)]
        count = [1  for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if arr[i]>arr[j] and dp[i]<dp[j]+1:
                    dp[i] = dp[j]+1
                    count[i] = count[j]
                elif arr[i]>arr[j] and dp[i]==dp[j]+1:
                    count[i] += count[j]
        maxi = max(dp)
        nos = 0
        for i in range(n):
            if dp[i] == maxi:
                nos+=count[i]

        return nos