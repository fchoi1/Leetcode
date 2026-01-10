class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        # 3 2 1 2 3

        # track lowests and things above it

        # pop out things in the stack when lower
        largest = 0
        stack = [] # height, idx


        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][0] > h:
                height, idx, _= stack.pop()
                largest = max(largest, height * (i - idx))
            stack.append((h,idx,i))

        if not stack:
            return largest
        
        N = stack[-1][2]
        # print(stack, largest, N)
        for h,idx,i in stack:
            # print(h, N-idx+1, i, idx)
            largest = max(largest, (N - idx + 1) * h, h * (i - idx + 1))

        return largest