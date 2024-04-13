class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # tuple hieght and index
        maxArea = 0
        for i,h in enumerate(heights):
            if stack and h < stack[-1][0]:
                while stack and h < stack[-1][0]:
                    height, index = stack.pop()
                    width = i - index
                    maxArea = max(maxArea, height * width)
                stack.append((h, index))
            else:
                stack.append((h,i))
        while stack:
            height, index = stack.pop()
            width = len(heights) - index
            maxArea = max(maxArea, height * width)
        return maxArea
