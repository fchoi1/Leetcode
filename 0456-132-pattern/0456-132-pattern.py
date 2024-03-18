class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        currMin = nums[0]
        for n in nums:
            while stack and n >= stack[-1][1]:
                stack.pop()
    
            if stack and stack[-1][0] < n < stack[-1][1]:
                return True

            currMin = min(currMin, n)
            stack.append((currMin, n))
        return False