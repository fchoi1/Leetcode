class Solution:
    def binaryGap(self, n: int) -> int:
        binStr = bin(n)[2:]
        # bit manipualation

        adj = None
        longest = 0

        for i, curr in enumerate(binStr):
            if curr == '1':
                if adj is not None:
                    longest = max(longest, i - adj)
                adj = i
        
        return longest