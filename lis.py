class Solution:
    def lowerbound(self, temp, target):
        low = 0
        high = len(temp)
        while low<high:
            mid = (low+high)//2
            if temp[mid]<target:
                low=mid+1
            else:
                high = mid
        return low


    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp = []
        temp.append(nums[0])

        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                index = self.lowerbound(temp, nums[i])
                temp[index] = nums[i]
        
        return len(temp)
        