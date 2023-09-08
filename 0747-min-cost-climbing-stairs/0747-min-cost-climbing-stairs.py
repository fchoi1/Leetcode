class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        length = len(cost)
        minCost = [cost[0],cost[1]]
        i = 2
        for price in cost[2:]:
            minCost.append( price + (min(minCost[i - 2] , minCost[i - 1])))
            i += 1
        return min(minCost[length-1], minCost[length-2])
        