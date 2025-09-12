class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        total = 0
        for char in s:
            total += int(char in vowels)
            
        starts_ends_with_vowel = s[0] in vowels or s[-1] in vowels
        has_consonants = len(s) - total > 0

        if total == 0:
            return False
        return True
        
        