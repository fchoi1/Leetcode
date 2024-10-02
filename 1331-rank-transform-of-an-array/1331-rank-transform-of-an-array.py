class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        order = {}
        for v, k in enumerate(sorted(set(arr))):
            order.setdefault(k, v + 1)
        return [order[n] for n in arr]

        