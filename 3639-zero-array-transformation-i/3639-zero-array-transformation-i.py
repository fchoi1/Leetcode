class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        counts = [0 for _ in range(len(nums)+1)]
        for s,e in queries:
            counts[s] += 1
            counts[e+1] -= 1

        curr = 0
        for c, n in zip(counts, nums):
            curr += c
            if curr < n:
                return False
        return True
        