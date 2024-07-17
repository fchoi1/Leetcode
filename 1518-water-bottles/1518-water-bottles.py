class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = empty = numBottles
        while empty >= numExchange:
            d,r = divmod(empty,numExchange) 
            total += d
            empty =  d + r
        return total
        
        