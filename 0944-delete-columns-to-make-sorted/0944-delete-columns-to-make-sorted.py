class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)

        cols = 0
        for i in range(len(strs[0])):
            prev = None
            for row in range(N):
                curr = strs[row][i]
                if not prev:
                    prev = curr
                else:
                    if curr < prev:
                        cols += 1
                        break
                    prev = curr

        return cols
        