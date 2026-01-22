class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # check each station
        # no


        # gas = 15
        # cost = 15
        if sum(gas) < sum(cost):
            return -1
        
        # there should be a solution

        currCost = 0
        currGas = 0
        idx = 0
        for i, (c, g) in enumerate(zip(cost, gas)):
            currCost += c
            currGas += g
            if currCost > currGas:
                idx = i + 1
                currCost = 0
                currGas = 0

        return idx 

        # gas  1 2 3 4 5
        # cost 5 4 3 2 1 