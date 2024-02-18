class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        length = -1
        for i, char in enumerate(s):
            if char in seen:
                length = max(length, i - seen[char] - 1)
            else:
                seen[char] = i
        return length