class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]]>=heights[i]):
                ht = heights[stack[-1]]
                stack.pop()
                width = 0
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] -1
                maxArea = max(maxArea, width*ht)
            stack.append(i)
        return maxArea

         