class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)

        remain = k % total
        for i,c in enumerate(chalk):
            remain -= c
            if remain < 0:
                return i
        return -1