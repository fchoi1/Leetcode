class Solution:
    def minimumLength(self, s: str) -> int:

        left = 0
        right = len(s) - 1
        
        while s[left] == s[right] and left < right:
            prev = s[left]

            while left < right and s[left] == prev:
                left += 1

            if left >= right:
                return 0
            while s[right] == prev:
                right -= 1
        return right - left + 1
                    