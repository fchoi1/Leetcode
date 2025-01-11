class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = Counter(s)
        odd = 0
        for c in count.values():
            if c % 2 == 1:
                odd += 1
            if odd > k:
                return False
        return odd <= k and len(s) >= k
            
