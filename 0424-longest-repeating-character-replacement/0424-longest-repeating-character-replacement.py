class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # 2 pointers
        slow = 0
        counts = [0] * 26
        maxLen = k

        for i in range(len(s)):
            char = ord(s[i]) - ord("A")
            counts[char] += 1
            while sum(counts) - max(counts) > k:
                index = ord(s[slow]) - ord("A")
                counts[index] -= 1
                slow += 1
            maxLen = max(maxLen, i - slow + 1)
        return maxLen


            
        