class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # drink as much as you can
        # can exchange 

        for i in range(1, numBottles // numExchange + 1):
            print(numBottles + i, (2 * numExchange + i) * (i+1) / 2 )
            if numBottles + i < (2 * numExchange + i) * (i+1) / 2:
                print("here", i)
                return numBottles + (i)
        return numBottles

        # 4 5 6 7 + 8 = 9 + 13 = 22 +. 8 = 30
        # (4 + 8) *  5 / 2  = 22

        # 7 * 2


        # 3 4 5 6 =. 18 -> 13
        # 10 + 4 