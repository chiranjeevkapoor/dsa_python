class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        temp = []
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])
        p = 0

        for i in range(len(temp)):
            nums[i] = temp[i]
            p+=1
        
        for i in range(p, n):
            nums[i]=0
        return nums