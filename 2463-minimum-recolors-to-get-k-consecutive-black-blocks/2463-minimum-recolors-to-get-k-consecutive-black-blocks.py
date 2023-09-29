class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        b = blocks[:k].count('B')
        minBlocks = k - b
        left = 0
        for right in range(k, len(blocks)):
            if blocks[right] == 'B':
                b += 1
            if blocks[right - k] == 'B':
                b -= 1
            minBlocks = min(minBlocks, k-b)
        return minBlocks
        