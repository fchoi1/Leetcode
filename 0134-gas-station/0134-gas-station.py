class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        diff = station = 0
        for i,(c, g)in enumerate(zip(cost, gas)):
            diff += g - c
            if diff < 0:
                station = i + 1
                diff = 0
        return station
