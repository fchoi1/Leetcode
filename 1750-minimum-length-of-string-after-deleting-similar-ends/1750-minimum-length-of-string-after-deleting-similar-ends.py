class Solution:
    def minimumLength(self, s: str) -> int:
        # pali
        letters = defaultdict(int)
        for c in s:
            letters[c] += 1
        seen = set()

        left = 0
        right = len(s) - 1
        
        while s[left] == s[right] and left < right:
            prev = s[left]
            letters.pop(s[left], None)
            seen.add(s[left])

            while left < right and s[left] == prev:
                left += 1

            if left >= right:
                return 0
            while s[right] == prev:
                right -= 1
        # print(right, left)
        return right - left + 1
                    