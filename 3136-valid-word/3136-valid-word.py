class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        hasVowel = False
        hasConsonant = False
        letters = "abcdefghijklmnopqrstuvwuxyz"
        nums = "1234567890"

        for char in word:
            if char.lower() not in letters and char not in nums:
                return False
            if char.lower() in 'aeuio':
                hasVowel = True
            elif char.lower() in letters:
                hasConsonant = True
        return hasVowel and hasConsonant
