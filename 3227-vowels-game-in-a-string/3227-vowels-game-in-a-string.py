class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        total = 0
        for char in s:
            total += char in vowels
            
        if total == 0:
            return False
        return True
        
        