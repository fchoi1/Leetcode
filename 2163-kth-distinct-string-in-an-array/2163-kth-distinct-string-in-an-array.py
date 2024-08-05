class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        c = 0
        for s in arr:
            if counts[s] > 1:
                continue
            else:
                c += 1
                if c == k:
                    return s
        return ""
