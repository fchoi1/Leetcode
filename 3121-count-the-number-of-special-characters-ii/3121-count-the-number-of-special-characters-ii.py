class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = 0
        upper = 0
        invalid = 0

        for ch in word:
            bit = 1 << (ord(ch.lower()) - ord('a'))

            if ch.islower():
                if upper & bit:
                    invalid |= bit
                lower |= bit
            else:
                upper |= bit

        return (lower & upper & ~invalid).bit_count()