class Solution:
    def getSecondLargest(self, arr):
        # code here
        n = len(arr)
        if n==0 or n==1:
            return -1
        
        largest = float('-inf')
        second_largest = float('-inf')
        
        for i in range(n):
            largest = max(arr[i], largest)
        
        for i in range(n):
            if arr[i] > second_largest and largest!=arr[i]:
                second_largest = arr[i]
        
        if second_largest == float('-inf'):
            return -1
        return second_largest