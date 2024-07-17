class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = empty = numBottles
        while empty >= numExchange:
            total += empty//numExchange
            empty =  empty // numExchange + empty % numExchange
        return total
        
        