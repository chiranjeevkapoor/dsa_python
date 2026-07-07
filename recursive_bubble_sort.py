class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        if n==1:
            return
        
        return self.bsort(arr, n)
    
    def bsort(self, arr, n):
        if n==1:
            return
        
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        self.bsort(arr, n-1)