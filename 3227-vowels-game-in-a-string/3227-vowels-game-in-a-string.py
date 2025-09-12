class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'

        counts = Counter(s)
        total = 0
        for char in vowels:
            total += counts[char]

        
        starts_ends_with_vowel = s[0] in vowels or s[-1] in vowels
        has_consonants = len(s) - total > 0

        if total == 0:
            return False
        
        
        if total % 2 == 1:
            return True
        else:
            return True

        # really only care about vowels
        