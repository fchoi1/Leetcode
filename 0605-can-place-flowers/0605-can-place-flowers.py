class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        i = 0
        left = None
        while i < len(flowerbed):
            
            right =  flowerbed[i + 1] if i + 1 < len(flowerbed) else 0

            if not left and not flowerbed[i] and not right:
                n -= 1
                flowerbed[i] = 1
            
            left = flowerbed[i]
            if n <= 0:
                return True
            i += 1

        return False
        