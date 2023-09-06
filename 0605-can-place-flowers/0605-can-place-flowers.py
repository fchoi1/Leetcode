class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        prev = 0  # Initialize prev as 0 (no flower before the first pot)
        size = len(flowerbed)

        for i in range(size):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  # Place a flower at the current position
                    count += 1

        return count >= n
        