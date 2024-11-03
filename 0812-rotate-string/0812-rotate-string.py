class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in s+s if len(s) <= len(goal) else False
        