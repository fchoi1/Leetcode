class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = extra = 0
        for char in s:
            if char == '(':
                opened += 1
            else:
                opened -= 1
            
            if opened < 0:
                extra += 1
                opened = 0
                
        return extra + opened
