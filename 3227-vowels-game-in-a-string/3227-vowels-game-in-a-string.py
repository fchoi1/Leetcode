class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        total = sum(char in vowels for char in s)
     
        if total == 0:
            return False
        return True
        
        