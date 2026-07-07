class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        return self.isort(arr, 1, n)
    
    def isort(self, arr, i, n):
        if i==n:
            return 
    
        j=i
        
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
        
        self.isort(arr, i+1, n)