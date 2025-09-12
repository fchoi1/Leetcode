class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        total = 0
        for char in s:
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                total += 1
            
        if total == 0:
            return False
        return True
        
        