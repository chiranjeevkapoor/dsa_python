class Solution:
    def getSecondLargest(self, arr):
        # code here
        n = len(arr)
        if n==0 or n==1:
            return -1
        
        
        largest = arr[0]
        slargest = -1
        
        for i in range(1, n):
            if arr[i]>largest:
                slargest = largest
                largest = arr[i]
            elif arr[i]>slargest and arr[i]!= largest:
                slargest=arr[i]
        return slargest