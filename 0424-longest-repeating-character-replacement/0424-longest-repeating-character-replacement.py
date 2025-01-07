class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        slow = fast = 0
        counts = [0] * 26
        maxLen = k

        while fast < len(s):
            char = ord(s[fast]) - ord("A")
            counts[char] += 1
            while sum(counts) - max(counts) > k:
                index = ord(s[slow]) - ord("A")
                counts[index] -= 1
                slow += 1
            maxLen = max(maxLen, fast - slow + 1)
            fast += 1
        return maxLen


            
        