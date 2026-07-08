class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if high is None:
            high = len(arr)-1
        
        if low<high:
            pivot_index = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot_index-1)
            self.quickSort(arr, pivot_index+1, high)
        return arr

    def partition(self, arr, low, high):
        # code here
        pivot = arr[high]
        i = low-1
        for j in range(low, high):
            if arr[j]<pivot:
                i +=1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        
        return i+1
        