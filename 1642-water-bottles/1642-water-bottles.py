class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        avail = numBottles
        drink = avail
        while avail >= numExchange:
            times = avail // numExchange
            remain = avail % numExchange
            avail = times + remain
            drink += times
        return drink 
        