class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        charSet = set()
        seen = set()
        
        for char in word:
            if char == char.upper():
                if char.lower() in charSet and char not in charSet:
                    seen.add(char.lower())
            else:
                if char.upper() in charSet:
                    seen.discard(char)
            charSet.add(char)
        return len(seen)