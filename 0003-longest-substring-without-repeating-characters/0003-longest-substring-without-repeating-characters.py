class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        maxLength = 0
        left = 0
        for char in s:
            while char in letters:
                letters.remove(s[left])
                left += 1
            letters.add(char)
            maxLength = max(maxLength, len(letters))
        return maxLength
        