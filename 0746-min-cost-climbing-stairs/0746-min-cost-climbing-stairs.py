class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cost[0]
        curr = cost[1]

        if len(cost) == 2:
            return min(prev, curr)
        
        for c in cost[2:]:
            temp = curr
            curr = min(curr, prev) + c
            prev = temp
        return min(curr, prev)
