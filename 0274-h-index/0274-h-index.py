class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i, c in enumerate(citations):
            if len(citations) - i >= c:
                h = c
            if c > i + 1:
                h = max(h, min(len(citations) - i, c))
        return h
    