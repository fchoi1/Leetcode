class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = set()
        lower = set()
        seen = set()
        for char in word:
            if char == char.upper():
                if char.lower() in lower:
                    seen.add(char.lower())
                upper.add(char)
            else:
                if char.upper() in upper:
                    seen.add(char)
                lower.add(char)
        return len(seen)