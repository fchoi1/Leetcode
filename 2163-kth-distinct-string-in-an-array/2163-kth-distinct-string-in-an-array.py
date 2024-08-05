class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = 0
        for s, counts in Counter(arr).items():
            if counts == 1:
                c += 1
                if c == k:
                    return s
        return ""
