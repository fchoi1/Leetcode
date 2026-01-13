class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        maxY = max(row[1] + row[2] for row in squares)

        l = 0
        r = maxY
        err = 10 ** -5

        def checkArea(yLimit):
            top = 0
            bottom = 0
            for x,y,l in squares:
                area = l * l
                if y >= yLimit:
                    top += area
                elif y + l <= yLimit:
                    bottom += area
                else:
                    ratio = (yLimit - y) / l
                    bottom += area * ratio
                    top += area * (1 - ratio)
            
            return (bottom, top)
        
        mid = 0
        while l < r and abs(r - l) > err:
            mid = (l + r) / 2

            bot, top = checkArea(mid)
            if top > bot:
                l = mid
            else:
                r = mid

        return mid

