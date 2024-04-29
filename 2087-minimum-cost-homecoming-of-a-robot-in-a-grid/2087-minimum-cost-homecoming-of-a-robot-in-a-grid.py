class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sY, sX = startPos
        hY, hX = homePos
        if sX == hX and sY == hY:
            return 0
        
        ySum = sum(rowCosts[min(sY, hY-1)+1: max(sY-1, hY)+1]) if sY != hY else 0
        xSum = sum(colCosts[min(sX, hX-1)+1: max(sX-1, hX)+1]) if sX != hX else 0
        return ySum + xSum


            