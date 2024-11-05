class Solution:
    def minChanges(self, s: str) -> int:
        
        c = 1
        prev = s[0]
        flip = 0
        for char in s[1:]:
            if char == prev:
                c += 1
            else:
                if c % 2 != 0:
                    flip += 1
                    c = 0
                else:
                    c = 1
            prev = char
        if c % 2 != 0:
            flip += 1
            c = 0
        else:
            c = 1    
        return flip

                
