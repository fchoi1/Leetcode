class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        avail = numBottles
        drink = avail
        while avail >= numExchange:
            avail -= (numExchange - 1) 
            numExchange += 1
            drink += 1
        return drink 
        