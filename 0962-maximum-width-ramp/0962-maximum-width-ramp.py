class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        \
        stack = []
        maxWidth = 0
        for i, n in enumerate(nums):
            if not stack or n < stack[-1][0]:
                stack.append((n,i))
            
        for i in range(len(nums)-1, -1, -1):
            left = nums[i]       
            while stack and left >= stack[-1][0]:
                _, j = stack.pop()
            maxWidth = max(maxWidth, i - j)

        return maxWidth