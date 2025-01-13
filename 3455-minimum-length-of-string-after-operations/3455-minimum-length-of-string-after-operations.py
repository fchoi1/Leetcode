class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        return sum(2 if count % 2 == 0 else 1 for count in c.values())