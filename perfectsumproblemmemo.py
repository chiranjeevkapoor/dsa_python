#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		n = len(arr)
		dp = [[-1 for _ in range(target+1)] for _ in range(n)]
		return self.solve(n-1, arr, target, dp)
		
	def solve(self, index, arr, target, dp):
	    if index == 0:
	        if target==0 and arr[0]==0:
	            return 2
	        if target==0 or arr[0] == target:
	            return 1
	        return 0
	    if dp[index][target] != -1:
	        return dp[index][target]
	    not_pick = self.solve(index-1, arr, target, dp)
	    pick = 0
	    if arr[index]<=target:
	        pick = self.solve(index-1, arr, target-arr[index], dp)
	    dp[index][target] = pick + not_pick
	    return pick + not_pick
		