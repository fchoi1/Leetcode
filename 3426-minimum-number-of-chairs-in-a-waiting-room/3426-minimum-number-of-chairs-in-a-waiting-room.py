class Solution:
    def minimumChairs(self, s: str) -> int:
        curr = 0
        start = 0
        for c in s:
            if c == 'E':
                curr -= 1
            else:
                curr += 1
            
            if curr < 0:
                start += 1
                curr += 1
        return start
                
        