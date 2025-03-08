class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        count = sum(b == 'W' for b in blocks[:k])
        minCount = count

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                count += 1
            
            if blocks[i - k] == 'W':
                count -= 1
            
            minCount = min(minCount, count)

        return minCount