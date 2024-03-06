class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        shift = list(range(26))
        if len(s) != len(t):
            return False
        seen = set()
        for start, end in zip(s, t):
            if start == end:
                continue
            diff = ord(end) - ord(start)
            if start > end:
                diff += 26
            if shift[diff] > k:
                return False
            shift[diff] += 26
            seen.add(diff)
        return True
        