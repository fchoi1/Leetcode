class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxD = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            maxD = max(maxD, count)
        return maxD
            
        