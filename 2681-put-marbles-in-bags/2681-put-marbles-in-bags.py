class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
   
        # calculate each pair sum for each division, k-1 divisions
        N = len(weights)
        pair_sum = []
        for prev, curr in zip(weights, weights[1:]):
            pair_sum.append(prev + curr)

        pair_sum.sort()


        return  sum(pair_sum[-k+1:]) - sum(pair_sum[:k-1])

