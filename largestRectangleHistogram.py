class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftSmaller = [0]*n
        rightSmaller = [0]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                leftSmaller[i] = 0
            else:
                leftSmaller[i] = stack[-1]+1
            stack.append(i)
        
        stack = []

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                rightSmaller[i] = n-1
            else:
                rightSmaller[i] = stack[-1]-1
            stack.append(i)
        
        maxArea = 0

        for i in range(n):
            maxArea = max(maxArea, (rightSmaller[i]-leftSmaller[i]+1)*heights[i])
        return maxArea



        