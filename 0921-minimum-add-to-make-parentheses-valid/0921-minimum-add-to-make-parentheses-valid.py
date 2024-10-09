class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        total = 0
        for b in s:
            if b == '(':
                opened += 1
            else:
                opened -= 1
            
            if opened < 0:
                total += 1
                opened = 0
        return opened + total
