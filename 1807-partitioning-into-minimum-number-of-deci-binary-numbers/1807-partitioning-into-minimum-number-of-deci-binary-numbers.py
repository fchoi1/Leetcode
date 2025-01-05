class Solution:
    def minPartitions(self, n: str) -> int:
        for c in '9876543210':
            if c in n:
                return int(c)
        
        return 0
        