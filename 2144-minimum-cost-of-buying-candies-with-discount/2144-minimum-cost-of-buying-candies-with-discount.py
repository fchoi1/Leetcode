class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # get the expensive for free

        cost.sort()
        total = 0
        N = len(cost)

        for i in range(N - 1, -1, -3):
            total += cost[i] 
            if i - 1 >= 0:
                total += cost[i - 1]

        return total